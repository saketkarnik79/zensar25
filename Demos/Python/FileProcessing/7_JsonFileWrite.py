import json

student = {
    "name": "Rahul",
    "age": 22,
    "course": "Python",
    "skills": [
        "Python",
        "SQL",
        "Azure"
    ]
}

with open("student.json", "w") as file:
    json.dump(student, file, indent=4)