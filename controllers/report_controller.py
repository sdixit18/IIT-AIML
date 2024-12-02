from flask import render_template
from models.excel_processor import ExcelProcessor
import os

def reports():
    # Define the path to the uploaded Excel file
    file_path = os.path.join('data', 'oil.xlsx')
    
    # Initialize the ExcelProcessor to read the data
    processor = ExcelProcessor(file_path)

    # Calculate different summaries based on the sheets
    sales_summary = processor.calculate_sales_summary()
    procurement_summary = processor.calculate_procurement_summary()
    labor_summary = processor.calculate_labor_summary()

    # Pass the data to the report page for rendering
    return render_template('reports.html', 
                           sales_summary=sales_summary['Total Sales'],
                           procurement_summary=procurement_summary['Total Procurement'],
                           labor_summary=labor_summary['Total Labor Cost'])
