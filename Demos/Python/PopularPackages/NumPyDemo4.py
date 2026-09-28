import numpy as np

numbers = np.arange(1, 13)

print("Original Array:")
print(numbers)

matrix = numbers.reshape(3, 4)

print("\n3 x 4 Matrix:")
print(matrix)

print("\nFlattened Array:")
print(matrix.flatten())