import pandas as pd

data = {
    "Name": ["Rahul", "Priya", "Amit", "Neha"],
    "Marks": [78, 92, 65, 88]
}

df = pd.DataFrame(data)

result = df.sort_values(
    by="Marks",
    ascending=False
)

print(result)