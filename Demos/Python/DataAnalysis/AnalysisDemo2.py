import pandas as pd
import openpyxl

# Load Excel file
df = pd.read_excel("employees.xlsx", sheet_name="Sheet1")

print(df)

# Display first 5 rows
print(df.head())