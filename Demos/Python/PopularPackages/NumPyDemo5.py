import numpy as np

marks = np.array([45, 78, 32, 89, 67, 91, 55])

print("All Marks:")
print(marks)

passed = marks[marks >= 40]
distinction = marks[marks >= 75]

print("\nPassed Students:")
print(passed)

print("\nDistinction Marks:")
print(distinction)