import numpy as np

# Generate 10 random marks between 40 and 100
marks = np.random.randint(40, 101, 10)

print("Random Marks:")
print(marks)

print("Average:", np.mean(marks))
print("Highest:", np.max(marks))
print("Lowest:", np.min(marks))