import pandas as pd

data = {
    "Name": ["Rahul", "Priya", "Amit", "Neha"],
    "Marks": [85, 92, 76, 88]
}

df = pd.DataFrame(data)

print("Student Data:")
print(df)
# df.describe()

print("\nAverage Marks:", df["Marks"].mean())
print("Highest Marks:", df["Marks"].max())