import pandas as pd

data = {
    "Name": ["Rahul", "Priya", "Amit", "Neha", "Rohan"],
    "Maths": [78, 92, 65, 88, 72],
    "Science": [82, 89, 70, 91, 75],
    "English": [75, 95, 68, 85, 78]
}

df = pd.DataFrame(data)

print("Student Data:")
print(df)

df["Total"] = df["Maths"] + df["Science"] + df["English"]
df["Average"] = df["Total"] / 3

print("\nResult:")
print(df)

print("Students with average above 80:")

# result = df[df["Average"] > 80]
result = df[
    (df["Maths"] >= 75) &
    (df["Science"] >= 80)
]

print(result)