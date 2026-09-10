from pathlib import Path
import json
import sqlite3
from tempfile import TemporaryDirectory
import pandas as pd
from src.report_generator import ReportGenerator


def run():
    with TemporaryDirectory() as folder:
        config = Path(folder) / "config.json"
        config.write_text(
            json.dumps({"output_directory": str(Path(folder) / "reports")})
        )
        generator = ReportGenerator(config)
        with sqlite3.connect(":memory:") as conn:
            pd.read_csv(Path(__file__).with_name("sales.csv")).to_sql(
                "sales", conn, index=False
            )
            analysis, _ = generator.generate_sales_analysis(conn)
        assert analysis["total_sales"] == 600
        return {
            "synthetic": True,
            "total_sales": float(analysis["total_sales"]),
            "total_orders": int(analysis["total_orders"]),
            "average_order_value": float(analysis["avg_order_value"]),
            "daily_average": float(analysis["daily_avg_sales"]),
            "months": list(analysis["monthly_trends"].index),
        }


if __name__ == "__main__":
    import json

    print(json.dumps(run(), ensure_ascii=False, indent=2, allow_nan=False))
