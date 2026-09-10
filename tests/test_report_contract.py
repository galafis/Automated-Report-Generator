import json
import sqlite3
import pandas as pd
import pytest
from src.report_generator import ReportGenerator


def generator(tmp_path):
    config = tmp_path / "config.json"
    config.write_text(json.dumps({"output_directory": str(tmp_path / "reports")}))
    return ReportGenerator(config)


def connection(rows):
    conn = sqlite3.connect(":memory:")
    pd.DataFrame(
        rows,
        columns=[
            "date",
            "sales_amount",
            "orders",
            "customers",
            "product_category",
            "region",
        ],
    ).to_sql("sales", conn, index=False)
    return conn


def test_partial_months_and_zero_orders(tmp_path):
    g = generator(tmp_path)
    with connection(
        [["2024-02-01", 0, 0, 0, "A", "North"], ["2025-02-01", 0, 0, 0, "A", "North"]]
    ) as conn:
        analysis, df = g.generate_sales_analysis(conn)
    assert analysis["avg_order_value"] == 0
    assert list(analysis["monthly_trends"].index) == ["2024-02", "2025-02"]
    assert g.create_visualizations(df, analysis).endswith(".png")


def test_daily_metrics_aggregate_multiple_rows(tmp_path):
    with connection(
        [
            ["2024-01-01", 10, 1, 1, "A", "N"],
            ["2024-01-01", 20, 2, 2, "B", "N"],
            ["2024-01-02", 40, 4, 4, "A", "N"],
        ]
    ) as conn:
        analysis, _ = generator(tmp_path).generate_sales_analysis(conn)
    assert analysis["daily_avg_sales"] == 35
    assert analysis["worst_day"]["sales_amount"] == 30


@pytest.mark.parametrize("amount", [-1, float("inf")])
def test_invalid_sales_rejected(tmp_path, amount):
    with connection([["2024-01-01", amount, 1, 1, "A", "N"]]) as conn:
        with pytest.raises(ValueError):
            generator(tmp_path).generate_sales_analysis(conn)


def test_empty_sales_rejected(tmp_path):
    with connection([]) as conn:
        with pytest.raises(ValueError):
            generator(tmp_path).generate_sales_analysis(conn)
