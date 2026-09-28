import matplotlib.pyplot as plt

months = ["Jan", "Feb", "Mar", "Apr", "May"]

product_a = [20, 25, 30, 35, 40]
product_b = [15, 20, 35, 30, 38]

plt.plot(months, product_a, marker="o", label="Product A")
plt.plot(months, product_b, marker="o", label="Product B")

plt.xlabel("Months")
plt.ylabel("Sales")
plt.title("Product Sales Comparison")

plt.legend()
plt.show()