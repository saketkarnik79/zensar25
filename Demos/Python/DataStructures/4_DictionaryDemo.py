# Dictionary creation
# employee = {
#     "id": "EMP001",
#     "name": "John Doe",
#     "age": 30,
#     "department": "Sales",
#     "salary": 50000,
#     "role": "Manager"
# }
# print("Employee Dictionary:", employee)
# print("Employee ID:", employee["id"]) # Output: Employee ID: EMP001

# using the get() method to access values
#print("Employee Name:", employee.get("name")) # Output: Employee Name: John Doe

# Dictionary CRUD Operations
# Create operation
employee = {
    "id": "EMP001",
    "name": "John Doe",
    "salary": 50000
}
# print(employee) # Output: {'id': 'EMP001', 'name': 'John Doe', 'salary': 50000}

# Read operation
# print(employee["name"]) # Output: John Doe
# print(employee.get("salary")) # Output: 50000

# Update operation
# employee["salary"] = 55000
# print(employee) # Output: {'id': 'EMP001', 'name': 'John Doe', 'salary': 55000}
# employee["department"] = "Sales"
# print(employee) # Output: {'id': 'EMP001', 'name': 'John Doe', 'salary': 55000, 'department': 'Sales'}

# Delete operation
# del employee["salary"]
# print(employee) # Output: {'id': 'EMP001', 'name': 'John Doe', 'department': 'Sales'}

# employee.pop("salary") # Remove salary key if it exists
# print(employee) # Output: {'id': 'EMP001', 'name': 'John Doe', 'department': 'Sales'}

# keys() example
# print(employee.keys()) # Output: dict_keys(['id', 'name', 'salary'])

# values() example
# print(employee.values()) # Output: dict_values(['EMP001', 'John Doe', 50000])

# items() example
# print(employee.items()) # Output: dict_items([('id', 'EMP001'), ('name', 'John Doe'), ('salary', 50000)])

# iterating through a dictionary
# for key, value in employee.items():
#     print(f"{key}: {value}")

# Dictionary update() method
# employee.update(
#     {
#         "name": "Jane Smith",
#         "age": 28,
#         "salary": 60000,
#     })
# print(employee) # Output: {'id': 'EMP001', 'name': 'Jane Smith', 'salary': 60000, 'age': 28}

# Checking if a key exists in the dictionary
# if "salary" in employee:
#     print("Salary key exists in the employee dictionary.")