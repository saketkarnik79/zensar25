import pandas as pd

data = {
    "Department": ["IT", "IT", "HR", "HR", "Sales", "Sales"],
    "Salary": [50000, 60000, 40000, 45000, 55000, 65000]
}

df = pd.DataFrame(data)

result = df.groupby("Department")["Salary"].agg(
    ["count", "sum", "mean", "min", "max"]
)

print(result)