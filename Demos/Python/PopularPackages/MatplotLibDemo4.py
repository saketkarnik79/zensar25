import matplotlib.pyplot as plt

subjects = ["English", "Maths", "Science", "Computer"]
marks = [25, 30, 20, 25]

plt.pie(marks, labels=subjects, autopct="%1.1f%%")

plt.title("Marks Distribution")

plt.show()