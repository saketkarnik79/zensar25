class Employee:
    def __init__(self, emp_id, name, department, salary):
        self.emp_id = emp_id
        self.name = name
        self.department = department
        self.salary = salary

    def display_details(self):
        print("\nEmployee Details")
        print(f"Employee ID: {self.emp_id}")
        print(f"Name       : {self.name}")
        print("Department  :", self.department)
        print("Salary      :", self.salary)

    def update_salary(self, new_salary):
        self.salary = new_salary
        print("Salary updated successfully!")

# Creating an Employee object
emp1 = Employee(101, "Rahul Sharma", "IT", 45000)

# Display employee details
emp1.display_details()

# Update salary
emp1.update_salary(50000)

# Display updated details
emp1.display_details()