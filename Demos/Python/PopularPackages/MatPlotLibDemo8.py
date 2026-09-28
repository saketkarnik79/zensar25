import matplotlib.pyplot as plt

marks = [45, 55, 60, 65, 70, 72, 75, 80, 85, 90, 95]

plt.boxplot(marks)

plt.ylabel("Marks")
plt.title("Student Marks Distribution")

plt.show()