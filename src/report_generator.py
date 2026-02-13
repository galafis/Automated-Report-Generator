#!/usr/bin/env python3
"""
Automated Report Generator
Advanced Python-based report generation system with multiple output formats,
data visualization, and automated scheduling capabilities.
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

from datetime import datetime, timedelta
import json
import sqlite3
from pathlib import Path
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
import schedule
import time

import plotly.graph_objects as go
import plotly.express as px
from reportlab.lib.pagesizes import letter, A4
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Paragraph, Spacer, Image
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch
from reportlab.lib import colors
import warnings
warnings.filterwarnings('ignore')

class ReportGenerator:
    def __init__(self, config_file='config.json'):
        """Initialize the report generator with configuration."""
        self.config = self.load_config(config_file)
        self.data_sources = {}
        self.output_dir = Path(self.config.get('output_directory', 'reports'))
        self.output_dir.mkdir(exist_ok=True)
        
    def load_config(self, config_file):
        """Load configuration from JSON file."""
        try:
            with open(config_file, 'r') as f:
                return json.load(f)
        except FileNotFoundError:
            return self.create_default_config()
    
    def create_default_config(self):
        """Create default configuration."""
        default_config = {
            "output_directory": "reports",
            "email_settings": {
                "smtp_server": "smtp.gmail.com",
                "smtp_port": 587,
                "sender_email": "",
                "sender_password": ""
            },
            "report_templates": {
                "sales_report": {
                    "title": "Sales Performance Report",
                    "frequency": "weekly",
                    "recipients": []
                },
                "financial_report": {
                    "title": "Financial Analysis Report",
                    "frequency": "monthly",
                    "recipients": []
                }
            }
        }
        with open('config.json', 'w') as f:
            json.dump(default_config, f, indent=2)
        return default_config
    
    def connect_database(self, db_path='sample_data.db'):
        """Connect to SQLite database and create sample data."""
        conn = sqlite3.connect(db_path)
        self.create_sample_data(conn)
        return conn
    
    def create_sample_data(self, conn):
        """Create sample data for demonstration."""
        # Sales data
        dates = pd.date_range(start='2024-01-01', end='2024-12-31', freq='D')
        sales_data = []
        
        for date in dates:
            # Simulate seasonal trends
            base_sales = 1000 + np.sin(date.dayofyear * 2 * np.pi / 365) * 200
            daily_sales = max(0, np.random.normal(base_sales, 150))
            
            sales_data.append({
                'date': date.strftime('%Y-%m-%d'),
                'sales_amount': round(daily_sales, 2),
                'orders': np.random.poisson(daily_sales / 50),
                'customers': np.random.poisson(daily_sales / 100),
                'product_category': np.random.choice(['Electronics', 'Clothing', 'Books', 'Home', 'Sports']),
                'region': np.random.choice(['North', 'South', 'East', 'West', 'Central'])
            })
        
        df_sales = pd.DataFrame(sales_data)
        df_sales.to_sql('sales', conn, if_exists='replace', index=False)
        
        # Customer data
        customer_data = []
        for i in range(1000):
            customer_data.append({
                'customer_id': f'CUST_{i:04d}',
                'age': np.random.randint(18, 80),
                'gender': np.random.choice(['M', 'F']),
                'location': np.random.choice(['Urban', 'Suburban', 'Rural']),
                'lifetime_value': round(np.random.exponential(500), 2),
                'acquisition_date': (datetime.now() - timedelta(days=np.random.randint(1, 365))).strftime('%Y-%m-%d')
            })
        
        df_customers = pd.DataFrame(customer_data)
        df_customers.to_sql('customers', conn, if_exists='replace', index=False)
        
        conn.commit()
    
    def load_data(self, query, conn):
        """Load data from database using SQL query."""
        return pd.read_sql_query(query, conn)
    
    def generate_sales_analysis(self, conn):
        """Generate comprehensive sales analysis."""
        # Load sales data
        sales_df = self.load_data("SELECT * FROM sales", conn)
        sales_df['date'] = pd.to_datetime(sales_df['date'])
        
        analysis = {
            'total_sales': sales_df['sales_amount'].sum(),
            'total_orders': sales_df['orders'].sum(),
            'avg_order_value': sales_df['sales_amount'].sum() / sales_df['orders'].sum(),
            'daily_avg_sales': sales_df['sales_amount'].mean(),
            'best_day': sales_df.loc[sales_df['sales_amount'].idxmax()],
            'worst_day': sales_df.loc[sales_df['sales_amount'].idxmin()],
            'monthly_trends': sales_df.groupby(sales_df['date'].dt.month).agg({
                'sales_amount': 'sum',
                'orders': 'sum',
                'customers': 'sum'
            }),
            'category_performance': sales_df.groupby('product_category')['sales_amount'].sum().sort_values(ascending=False),
            'regional_performance': sales_df.groupby('region')['sales_amount'].sum().sort_values(ascending=False)
        }
        
        return analysis, sales_df
    
    def create_visualizations(self, sales_df, analysis):
        """Create various visualizations for the report."""
        try:
            plt.style.use('seaborn-v0_8')
        except OSError:
            try:
                plt.style.use('seaborn')
            except OSError:
                plt.style.use('ggplot')
        fig, axes = plt.subplots(2, 2, figsize=(15, 12))
        
        # Daily sales trend
        daily_sales = sales_df.groupby('date')['sales_amount'].sum()
        axes[0, 0].plot(daily_sales.index, daily_sales.values, linewidth=2, color='#2E86AB')
        axes[0, 0].set_title('Daily Sales Trend', fontsize=14, fontweight='bold')
        axes[0, 0].set_xlabel('Date')
        axes[0, 0].set_ylabel('Sales Amount ($)')
        axes[0, 0].grid(True, alpha=0.3)
        
        # Category performance
        category_data = analysis['category_performance']
        axes[0, 1].bar(category_data.index, category_data.values, color='#A23B72')
        axes[0, 1].set_title('Sales by Product Category', fontsize=14, fontweight='bold')
        axes[0, 1].set_xlabel('Category')
        axes[0, 1].set_ylabel('Sales Amount ($)')
        axes[0, 1].tick_params(axis='x', rotation=45)
        
        # Regional performance
        regional_data = analysis['regional_performance']
        axes[1, 0].pie(regional_data.values, labels=regional_data.index, autopct='%1.1f%%', 
                       colors=['#F18F01', '#C73E1D', '#2E86AB', '#A23B72', '#F24236'])
        axes[1, 0].set_title('Sales Distribution by Region', fontsize=14, fontweight='bold')
        
        # Monthly trends
        monthly_data = analysis['monthly_trends']
        months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 
                 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
        axes[1, 1].bar(months, monthly_data['sales_amount'].values, color='#F18F01')
        axes[1, 1].set_title('Monthly Sales Performance', fontsize=14, fontweight='bold')
        axes[1, 1].set_xlabel('Month')
        axes[1, 1].set_ylabel('Sales Amount ($)')
        axes[1, 1].tick_params(axis='x', rotation=45)
        
        plt.tight_layout()
        chart_path = self.output_dir / 'sales_analysis_charts.png'
        plt.savefig(chart_path, dpi=300, bbox_inches='tight')
        plt.close()
        
        return str(chart_path)
    
    def create_interactive_dashboard(self, sales_df, analysis):
        """Create interactive Plotly dashboard."""
        # Create subplots
        from plotly.subplots import make_subplots
        
        fig = make_subplots(
            rows=2, cols=2,
            subplot_titles=('Daily Sales Trend', 'Category Performance', 
                          'Regional Distribution', 'Monthly Trends'),
            specs=[[{"secondary_y": False}, {"secondary_y": False}],
                   [{"type": "pie"}, {"secondary_y": False}]]
        )
        
        # Daily sales trend
        daily_sales = sales_df.groupby('date')['sales_amount'].sum()
        fig.add_trace(
            go.Scatter(x=daily_sales.index, y=daily_sales.values, 
                      mode='lines', name='Daily Sales', line=dict(color='#2E86AB')),
            row=1, col=1
        )
        
        # Category performance
        category_data = analysis['category_performance']
        fig.add_trace(
            go.Bar(x=category_data.index, y=category_data.values, 
                   name='Category Sales', marker_color='#A23B72'),
            row=1, col=2
        )
        
        # Regional distribution
        regional_data = analysis['regional_performance']
        fig.add_trace(
            go.Pie(labels=regional_data.index, values=regional_data.values, 
                   name="Regional Sales"),
            row=2, col=1
        )
        
        # Monthly trends
        monthly_data = analysis['monthly_trends']
        months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 
                 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
        fig.add_trace(
            go.Bar(x=months, y=monthly_data['sales_amount'].values, 
                   name='Monthly Sales', marker_color='#F18F01'),
            row=2, col=2
        )
        
        fig.update_layout(height=800, showlegend=False, 
                         title_text="Sales Performance Dashboard")
        
        dashboard_path = self.output_dir / 'interactive_dashboard.html'
        fig.write_html(str(dashboard_path))
        
        return str(dashboard_path)
    
    def generate_pdf_report(self, analysis, chart_path):
        """Generate PDF report using ReportLab."""
        pdf_path = self.output_dir / f'sales_report_{datetime.now().strftime("%Y%m%d")}.pdf'
        doc = SimpleDocTemplate(str(pdf_path), pagesize=A4)
        styles = getSampleStyleSheet()
        story = []
        
        # Title
        title_style = ParagraphStyle(
            'CustomTitle',
            parent=styles['Heading1'],
            fontSize=24,
            spaceAfter=30,
            textColor=colors.HexColor('#2E86AB'),
            alignment=1  # Center alignment
        )
        story.append(Paragraph("Sales Performance Report", title_style))
        story.append(Spacer(1, 20))
        
        # Executive Summary
        story.append(Paragraph("Executive Summary", styles['Heading2']))
        summary_text = f"""
        This report provides a comprehensive analysis of sales performance for the current period.
        Key highlights include:
        <br/><br/>
        • Total Sales: ${analysis['total_sales']:,.2f}<br/>
        • Total Orders: {analysis['total_orders']:,}<br/>
        • Average Order Value: ${analysis['avg_order_value']:.2f}<br/>
        • Daily Average Sales: ${analysis['daily_avg_sales']:.2f}<br/>
        """
        story.append(Paragraph(summary_text, styles['Normal']))
        story.append(Spacer(1, 20))
        
        # Key Metrics Table
        story.append(Paragraph("Key Performance Indicators", styles['Heading2']))
        
        kpi_data = [
            ['Metric', 'Value'],
            ['Total Sales', f"${analysis['total_sales']:,.2f}"],
            ['Total Orders', f"{analysis['total_orders']:,}"],
            ['Average Order Value', f"${analysis['avg_order_value']:.2f}"],
            ['Daily Average Sales', f"${analysis['daily_avg_sales']:.2f}"],
            ['Best Sales Day', f"${analysis['best_day']['sales_amount']:.2f}"],
            ['Worst Sales Day', f"${analysis['worst_day']['sales_amount']:.2f}"]
        ]
        
        kpi_table = Table(kpi_data, colWidths=[3*inch, 2*inch])
        kpi_table.setStyle(TableStyle([
            ('BACKGROUND', (0, 0), (-1, 0), colors.HexColor('#2E86AB')),
            ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
            ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
            ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
            ('FONTSIZE', (0, 0), (-1, 0), 12),
            ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
            ('BACKGROUND', (0, 1), (-1, -1), colors.beige),
            ('GRID', (0, 0), (-1, -1), 1, colors.black)
        ]))
        
        story.append(kpi_table)
        story.append(Spacer(1, 20))
        
        # Charts
        if Path(chart_path).exists():
            story.append(Paragraph("Performance Charts", styles['Heading2']))
            story.append(Image(chart_path, width=6*inch, height=4.5*inch))
        
        doc.build(story)
        return str(pdf_path)
    
    def send_email_report(self, pdf_path, recipients):
        """Send email with PDF report attachment."""
        if not recipients or not self.config['email_settings']['sender_email']:
            print("Email configuration incomplete. Skipping email send.")
            return
        
        msg = MIMEMultipart()
        msg['From'] = self.config['email_settings']['sender_email']
        msg['To'] = ', '.join(recipients)
        msg['Subject'] = f"Sales Report - {datetime.now().strftime('%Y-%m-%d')}"
        
        body = """
        Dear Team,
        
        Please find attached the latest sales performance report.
        
        Key highlights:
        - Comprehensive sales analysis
        - Performance visualizations
        - Regional and category breakdowns
        
        Best regards,
        Automated Report System
        """
        
        msg.attach(MIMEText(body, 'plain'))
        
        # Attach PDF
        with open(pdf_path, "rb") as attachment:
            part = MIMEBase('application', 'octet-stream')
            part.set_payload(attachment.read())
        
        encoders.encode_base64(part)
        part.add_header(
            'Content-Disposition',
            f'attachment; filename= {Path(pdf_path).name}'
        )
        msg.attach(part)
        
        # Send email
        try:
            server = smtplib.SMTP(self.config['email_settings']['smtp_server'], 
                                self.config['email_settings']['smtp_port'])
            server.starttls()
            server.login(self.config['email_settings']['sender_email'], 
                        self.config['email_settings']['sender_password'])
            text = msg.as_string()
            server.sendmail(self.config['email_settings']['sender_email'], recipients, text)
            server.quit()
            print(f"Email sent successfully to {recipients}")
        except Exception as e:
            print(f"Failed to send email: {str(e)}")
    
    def generate_full_report(self):
        """Generate complete report with all components."""
        print("Starting report generation...")
        
        # Connect to database
        conn = self.connect_database()
        
        # Generate analysis
        analysis, sales_df = self.generate_sales_analysis(conn)
        
        # Create visualizations
        chart_path = self.create_visualizations(sales_df, analysis)
        
        # Create interactive dashboard
        dashboard_path = self.create_interactive_dashboard(sales_df, analysis)
        
        # Generate PDF report
        pdf_path = self.generate_pdf_report(analysis, chart_path)
        
        # Send email (if configured)
        recipients = self.config['report_templates']['sales_report']['recipients']
        if recipients:
            self.send_email_report(pdf_path, recipients)
        
        conn.close()
        
        print(f"Report generation completed!")
        print(f"PDF Report: {pdf_path}")
        print(f"Interactive Dashboard: {dashboard_path}")
        print(f"Charts: {chart_path}")
        
        return {
            'pdf_report': pdf_path,
            'dashboard': dashboard_path,
            'charts': chart_path,
            'analysis': analysis
        }
    
    def schedule_reports(self):
        """Schedule automated report generation."""
        # Schedule weekly sales report
        schedule.every().monday.at("09:00").do(self.generate_full_report)
        
        # Schedule monthly financial report (every 30 days)
        schedule.every(30).days.do(self.generate_full_report)
        
        print("Report scheduling activated. Reports will be generated automatically.")
        print("Weekly reports: Every Monday at 9:00 AM")
        print("Monthly reports: First day of each month")
        
        while True:
            schedule.run_pending()
            time.sleep(60)  # Check every minute

def main():
    """Main function to run the report generator."""
    generator = ReportGenerator()
    
    # Generate immediate report
    results = generator.generate_full_report()
    
    # Optionally start scheduler
    # generator.schedule_reports()

if __name__ == "__main__":
    main()

