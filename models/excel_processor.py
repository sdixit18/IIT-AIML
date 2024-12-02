import pandas as pd

class ExcelProcessor:
    def __init__(self, file_path):
        self.file_path = file_path
        self.data = pd.read_excel(self.file_path, sheet_name=None)  # Read all sheets

    def calculate_sales_summary(self):
        # Assuming the sheet is named 'Sales' and has a column 'Sales'
        sales_data = self.data['Sales']
        total_sales = sales_data['Sales'].sum()  # Sum of all sales
        return {'Total Sales': total_sales}

    def calculate_procurement_summary(self):
        # Assuming the sheet is named 'Procurement' and has a column 'Procurement'
        procurement_data = self.data['Procurement']
        total_procurement = procurement_data['Procurement'].sum()  # Sum of all procurement
        return {'Total Procurement': total_procurement}

    def calculate_labor_summary(self):
        # Assuming the sheet is named 'Labor' and has a column 'Labor Cost'
        labor_data = self.data['Labor']
        total_labor_cost = labor_data['Labor Cost'].sum()  # Sum of all labor costs
        return {'Total Labor Cost': total_labor_cost}
