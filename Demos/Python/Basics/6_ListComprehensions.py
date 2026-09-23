# numbers = []
# for i in range(1, 11):
#     numbers.append(i * 2) # This will create a list of even numbers from 2 to 20
# print(numbers)  # Output: [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]

# List comprehension to create a list of even numbers from 2 to 20

# marks = [35, 67, 82, 45, 91, 28]

# result = [
#     "Pass" if mark >= 50 else "Fail"
#     for mark in marks
# ]

# print(result)

salaries = [30000, 45000, 50000, 60000, 75000]

bonuses = [salary * 0.10 for salary in salaries]

print(bonuses)