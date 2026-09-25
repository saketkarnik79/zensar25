import csv
students = [
    [101, "Rahul", "Python"],
    [102, "Priya", "Java"],
    [103, "Amit", "C#"]
]

with open("students2.csv", "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(["ID", "Name", "Course"])
    writer.writerows(students)