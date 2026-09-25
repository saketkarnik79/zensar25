import json

students = [
    {
        "id": 101,
        "name": "Rahul",
        "course": "Python"
    },
    {
        "id": 102,
        "name": "Priya",
        "course": "Java"
    },
    {
        "id": 103,
        "name": "Amit",
        "course": "C#"
    }
]

with open("students.json", "w") as file:
    json.dump(students, file, indent=4)