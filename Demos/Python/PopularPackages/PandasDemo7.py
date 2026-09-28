import pandas as pd

students = pd.DataFrame({
    "StudentID": [101, 102, 103],
    "Name": ["Rahul", "Priya", "Amit"]
})

marks = pd.DataFrame({
    "StudentID": [101, 102, 103],
    "Marks": [85, 92, 78]
})

result = pd.merge(
    students,
    marks,
    on="StudentID"
)

print(result)