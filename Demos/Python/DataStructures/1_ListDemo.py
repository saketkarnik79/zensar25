# students = [] # Empty list to store student names
# print(students) # Output: []

# student = ["Alice", "Bob", "Charlie", "James"] # List of student names
# print(student) # Output: ['Alice', 'Bob', 'Charlie', 'James']

# marks = [85, 90, 78, 92] # List of student marks
# print(marks) # Output: [85, 90, 78, 92]

# employee = ["EMP001", "James", 35, "Manager", 75000.0, True] # List of employee details
# print(employee) # Output: ['EMP001', 'James', 35, 'Manager', 75000.0, True]

# name = "John Doe" # String variable
# characters = list(name) # Convert string to list of characters
# print(characters) # Output: ['J', 'o', 'h', 'n', ' ', 'D', 'o', 'e']

# List length
# students = ["Alice", "Bob", "Charlie", "James"]
# print(len(students)) # Output: 4
# print(students[0]) # Output: Alice
# print(students[1]) # Output: Bob
# print(students[2]) # Output: Charlie
# print(students[3]) # Output: James
# print(students[4]) # Output: IndexError: list index out of range

# print(students[-1]) # Output: James
# print(students[-2]) # Output: Charlie
# print(students[-3]) # Output: Bob
# print(students[-4]) # Output: Alice

# Update student at index 1
# students[1] = "David"
# print(students) # Output: ['Alice', 'David', 'Charlie', 'James']

# Slicing example
# print(students[1:3]) # Output: ['David', 'Charlie']
# print(students[:2]) # Output: ['Alice', 'David']
# print(students[2:]) # Output: ['Charlie', 'James']

# Example for slicing with step
# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# print(numbers[1:6:2]) # Output: [2, 4, 6]

# Example for reversing a list
# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# numbers.reverse()
# print(numbers) # Output: [9, 8, 7, 6, 5, 4, 3, 2, 1]

# Example for reversing a list using slicing
# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# reversed_numbers = numbers[::-1]
# print(reversed_numbers) # Output: [9, 8, 7, 6, 5, 4, 3, 2, 1]

# Example for sorting a list
numbers = [5, 2, 9, 1, 5, 6]
numbers.sort()
print(numbers) # Output: [1, 2, 5, 5, 6, 9]