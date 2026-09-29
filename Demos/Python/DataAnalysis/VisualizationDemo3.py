import matplotlib.pyplot as plt

departments = ["IT", "HR", "Finance", "Sales"]
employees = [25, 15, 10, 30]

plt.pie(
    employees,
    labels=departments,
    autopct="%1.1f%%"
)

plt.title("Employee Distribution by Department")

plt.show()