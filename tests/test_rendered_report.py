from pathlib import Path
from examples.render_report import render


def test_full_local_render(tmp_path):
    paths = render(tmp_path)
    assert Path(paths["pdf"]).read_bytes().startswith(b"%PDF-")
    assert Path(paths["chart"]).stat().st_size > 1000
    assert "plotly" in Path(paths["dashboard"]).read_text(encoding="utf-8").lower()
