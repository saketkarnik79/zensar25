import pandas as pd

data = {
    "Employee": ["Amit", "Rahul", "Priya", "Neha", "Rohan", "Sneha"],
    "Department": ["IT", "HR", "IT", "HR", "Sales", "Sales"],
    "Salary": [50000, 40000, 60000, 45000, 55000, 65000]
}

df = pd.DataFrame(data)

print("Employee Data:")
print(df)

result = df.groupby("Department")["Salary"].mean()

print("\nAverage Salary Department-wise:")
print(result)