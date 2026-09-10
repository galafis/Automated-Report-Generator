"""Render the supplied synthetic sales fixture; no email or scheduler calls."""

import argparse
import json
import sqlite3
from pathlib import Path
from tempfile import TemporaryDirectory
import pandas as pd
from src.report_generator import ReportGenerator


def render(output_dir):
    output_dir = Path(output_dir).resolve()
    with TemporaryDirectory() as folder:
        config = Path(folder) / "config.json"
        config.write_text(json.dumps({"output_directory": str(output_dir)}))
        generator = ReportGenerator(config)
        with sqlite3.connect(":memory:") as conn:
            pd.read_csv(Path(__file__).with_name("sales.csv")).to_sql(
                "sales", conn, index=False
            )
            analysis, frame = generator.generate_sales_analysis(conn)
        chart = generator.create_visualizations(frame, analysis)
        dashboard = generator.create_interactive_dashboard(frame, analysis)
        pdf = generator.generate_pdf_report(analysis, chart, synthetic=True)
        assert Path(pdf).read_bytes().startswith(b"%PDF-")
        return {"pdf": pdf, "chart": chart, "dashboard": dashboard}


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Render synthetic report / Gerar relatório fictício"
    )
    parser.add_argument("--output-dir", default="reports/example")
    print(json.dumps(render(parser.parse_args().output_dir), indent=2))
