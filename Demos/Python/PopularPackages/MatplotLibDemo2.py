import matplotlib.pyplot as plt

months = ["Jan", "Feb", "Mar", "Apr", "May"]
sales = [20000, 25000, 22000, 30000, 35000]

plt.plot(months, sales, marker="o")

plt.xlabel("Month")
plt.ylabel("Sales")
plt.title("Monthly Sales")

plt.show()