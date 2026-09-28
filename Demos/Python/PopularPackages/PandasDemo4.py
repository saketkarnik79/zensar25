import pandas as pd
import numpy as np

data = {
    "Name": ["Rahul", "Priya", "Amit", "Neha"],
    "Marks": [78, np.nan, 65, 88]
}

df = pd.DataFrame(data)

print("Original Data:")
print(df)

print("\nMissing Values:")
print(df.isnull())

# Replace missing value with average
df["Marks"] = df["Marks"].fillna(df["Marks"].mean())

print("\nAfter Handling Missing Data:")
print(df)