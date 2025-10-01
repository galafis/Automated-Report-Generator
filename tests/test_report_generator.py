
import unittest
import os
from src.report_generator import ReportGenerator

class TestReportGenerator(unittest.TestCase):
    def setUp(self):
        self.report_generator = ReportGenerator()

    def test_create_default_config(self):
        config = self.report_generator.create_default_config()
        self.assertIn("output_directory", config)
        self.assertEqual(config["output_directory"], "reports")

    def test_connect_database_and_create_sample_data(self):
        conn = self.report_generator.connect_database(db_path=":memory:")
        cursor = conn.cursor()
        cursor.execute("SELECT name FROM sqlite_master WHERE type=\'table\';")
        tables = cursor.fetchall()
        self.assertIn(("sales",), tables)
        self.assertIn(("customers",), tables)
        conn.close()

    def test_generate_sales_analysis(self):
        conn = self.report_generator.connect_database(db_path=":memory:")
        analysis, sales_df = self.report_generator.generate_sales_analysis(conn)
        self.assertIn("total_sales", analysis)
        self.assertGreater(analysis["total_sales"], 0)
        conn.close()

if __name__ == '__main__':
    unittest.main()

