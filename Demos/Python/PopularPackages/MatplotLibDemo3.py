import matplotlib.pyplot as plt

students = ["Rahul", "Priya", "Amit", "Neha"]
marks = [75, 90, 65, 85]

plt.barh(students, marks)

plt.xlabel("Marks")
plt.ylabel("Students")
plt.title("Student Marks")

plt.show()