import matplotlib.pyplot as plt

hours = [1, 2, 3, 4, 5]
users = [10, 20, 20, 35, 40]

plt.step(hours, users)

plt.xlabel("Hours")
plt.ylabel("Users")
plt.title("Users Over Time")

plt.show()