import pandas as pd
import matplotlib.pyplot as plt

# --------------------------------
# 1. Create Sales Data
# --------------------------------

data = {
    "Month": ["Jan", "Feb", "Mar", "Apr", "May", "Jun"],
    "Sales": [50000, 65000, 58000, 72000, 85000, 90000],
    "Profit": [10000, 15000, 12000, 18000, 22000, 25000],
    "Orders": [120, 150, 135, 170, 190, 210]
}

df = pd.DataFrame(data)

print("===== SALES DATA =====")
print(df)


# --------------------------------
# 2. Sales Summary
# --------------------------------

total_sales = df["Sales"].sum()
average_sales = df["Sales"].mean()
total_profit = df["Profit"].sum()
total_orders = df["Orders"].sum()

print("\n===== SALES DASHBOARD =====")

print("Total Sales     : ₹", total_sales)
print("Average Sales   : ₹", round(average_sales, 2))
print("Total Profit    : ₹", total_profit)
print("Total Orders    :", total_orders)


# --------------------------------
# 3. Find Highest Sales Month
# --------------------------------

highest_sales = df.loc[df["Sales"].idxmax()]

print("\n===== BEST PERFORMING MONTH =====")

print("Month :", highest_sales["Month"])
print("Sales : ₹", highest_sales["Sales"])


# --------------------------------
# 4. Find Lowest Sales Month
# --------------------------------

lowest_sales = df.loc[df["Sales"].idxmin()]

print("\n===== LOWEST SALES MONTH =====")

print("Month :", lowest_sales["Month"])
print("Sales : ₹", lowest_sales["Sales"])


# --------------------------------
# 5. Filter High Sales Months
# --------------------------------

high_sales = df[df["Sales"] > 70000]

print("\n===== MONTHS WITH SALES ABOVE ₹70,000 =====")
print(high_sales)


# --------------------------------
# 6. Line Chart - Monthly Sales
# --------------------------------

plt.figure(figsize=(8, 5))

plt.plot(
    df["Month"],
    df["Sales"],
    marker="o"
)

plt.title("Monthly Sales Trend")
plt.xlabel("Month")
plt.ylabel("Sales (₹)")
plt.grid()

plt.show()


# --------------------------------
# 7. Bar Chart - Monthly Profit
# --------------------------------

plt.figure(figsize=(8, 5))

plt.bar(
    df["Month"],
    df["Profit"]
)

plt.title("Monthly Profit")
plt.xlabel("Month")
plt.ylabel("Profit (₹)")

plt.show()


# --------------------------------
# 8. Pie Chart - Sales Distribution
# --------------------------------

plt.figure(figsize=(7, 7))

plt.pie(
    df["Sales"],
    labels=df["Month"],
    autopct="%1.1f%%"
)

plt.title("Sales Distribution by Month")

plt.show()


# --------------------------------
# 9. Bar Chart - Monthly Orders
# --------------------------------

plt.figure(figsize=(8, 5))

plt.bar(
    df["Month"],
    df["Orders"]
)

plt.title("Monthly Orders")
plt.xlabel("Month")
plt.ylabel("Number of Orders")

plt.show()