from pathlib import Path
from examples.render_report import render
from pypdf import PdfReader
from test_report_contract import generator, connection
import pytest


def test_full_local_render(tmp_path):
    paths = render(tmp_path)
    assert Path(paths["pdf"]).read_bytes().startswith(b"%PDF-")
    assert Path(paths["chart"]).stat().st_size > 1000
    assert "plotly" in Path(paths["dashboard"]).read_text(encoding="utf-8").lower()
    text = "\n".join(page.extract_text() for page in PdfReader(paths["pdf"]).pages)
    assert "SYNTHETIC WORKED EXAMPLE" in text


def test_supplied_data_is_not_automatically_labelled_synthetic(tmp_path):
    report = generator(tmp_path)
    with connection([["2026-01-01", 100, 2, 1, "A", "N"]]) as conn:
        analysis, _ = report.generate_sales_analysis(conn)
    path = report.generate_pdf_report(analysis, tmp_path / "absent-chart.png")
    text = "\n".join(page.extract_text() for page in PdfReader(path).pages)
    assert "SUPPLIED DATA" in text
    assert "DADOS FORNECIDOS" in text
    assert "SYNTHETIC WORKED EXAMPLE" not in text
    assert "No real company performance" not in text


def test_provenance_flag_rejects_ambiguous_string(tmp_path):
    with pytest.raises(ValueError):
        generator(tmp_path).generate_pdf_report({}, "absent.png", synthetic="false")
