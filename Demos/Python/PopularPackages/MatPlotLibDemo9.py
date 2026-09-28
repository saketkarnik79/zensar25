import matplotlib.pyplot as plt

days = [1, 2, 3, 4, 5]
sales = [10, 25, 15, 30, 20]

plt.stem(days, sales)

plt.xlabel("Day")
plt.ylabel("Sales")
plt.title("Daily Sales")

plt.show()