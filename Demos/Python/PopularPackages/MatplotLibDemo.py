import matplotlib.pyplot as plt

students = ["Rahul", "Priya", "Amit", "Neha"]
marks = [85, 92, 76, 88]

plt.bar(students, marks)

plt.xlabel("Students")
plt.ylabel("Marks")
plt.title("Student Marks")

plt.show()