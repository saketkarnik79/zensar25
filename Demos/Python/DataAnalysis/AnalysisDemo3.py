import pandas as pd

data = {
    "Name": ["Amit", "Priya", "Rahul", "Sneha", "Rohan"],
    "Department": ["IT", "HR", "IT", "Finance", "HR"],
    "Salary": [50000, 45000, 60000, 55000, 48000]
}

df = pd.DataFrame(data)

print(df)

# employees from IT Department
it_employees = df[df["Department"] == "IT"]
print(it_employees)

# employees with Salary Greater than ₹50000
high_salary = df[df["Salary"] > 50000]
print(high_salary)

# multiple conditions
result = df[
    (df["Department"] == "IT") &
    (df["Salary"] > 50000)
]
print(result)

# Data Analysis - Grouping
grouped = df.groupby("Department")

for department, employees in grouped:
    print("\nDepartment:", department)
    print(employees)

# Average Salary by department
average_salary = df.groupby("Department")["Salary"].mean()
print(average_salary)

# Data Analysis - Aggregation
print("Total Salary:")
print(df["Salary"].sum())

print("Average Salary:")
print(df["Salary"].mean())

print("Minimum Salary:")
print(df["Salary"].min())

print("Maximum Salary:")
print(df["Salary"].max())

print("Number of Employees:")
print(df["Salary"].count())

# Combined Aggregation
result = df["Salary"].agg([
    "sum",
    "mean",
    "min",
    "max",
    "count"
])

print(result)

# Aggregation with grouping
result = df.groupby("Department")["Salary"].agg([
    "sum",
    "mean",
    "min",
    "max",
    "count"
])

print(result)