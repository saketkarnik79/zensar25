import matplotlib.pyplot as plt

months = ["Jan", "Feb", "Mar", "Apr", "May"]
sales = [20, 25, 22, 30, 35]

plt.fill_between(months, sales, alpha=0.5)

plt.xlabel("Months")
plt.ylabel("Sales")
plt.title("Monthly Sales")

plt.show()