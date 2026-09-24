# Tuple creation
# employee = ("EMP001", "John Doe", 30, "Software Engineer", 75000.0)
# print(employee) # Output: ('EMP001', 'John Doe', 30, 'Software Engineer', 75000.0)

# Single element tuple
# single_element_tuple = ("Single Element",)
# print(single_element_tuple) # Output: ('Single Element',)
# print(type(single_element_tuple)) # Output: <class 'tuple'>

# Tuple indexing
employee = ("EMP001", "John Doe", 30, "Software Engineer", 75000.0)
# print(employee[0]) # Output: EMP001  
# print(employee[1]) # Output: John Doe
# print(employee[2]) # Output: 30
# print(employee[3]) # Output: Software Engineer
# print(employee[4]) # Output: 75000.0
# employee[1] = "Jane Smith" # This will raise a TypeError since tuples are immutable
# print(employee) # Output: ('EMP001', 'John Doe', 30, 'Software Engineer', 75000.0)

# Concatenation of tuples
# tuple1 = (1, 2, 3,)
# tuple2 = (4, 5, 6)
# tuple3 = tuple1 + tuple2
# print(tuple3) # Output: (1, 2, 3, 4, 5, 6)

# Repetition of tuples
# tuple1 = (1, 2, 3)
# tuple2 = tuple1 * 3
# print(tuple2) # Output: (1, 2, 3, 1, 2, 3, 1, 2, 3)

# Membership testing
# tuple1 = (1, 2, 3, 4, 5)
# print(3 in tuple1) # Output: True
# print(6 in tuple1) # Output: False

# Tuple unpacking (object destructuring)
employee = ("EMP001", "John Doe", 30, "Software Engineer", 75000.0)
emp_id, name, age, position, salary = employee
print(emp_id) # Output: EMP001
print(name) # Output: John Doe
print(age) # Output: 30
print(position) # Output: Software Engineer
print(salary) # Output: 75000.0