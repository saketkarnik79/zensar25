class Person:
    def display_person(self):
        print("This is a person")

class Employee(Person):
    def display_employee(self):
        print("This is an employee")

class Manager(Employee):
    def display_manager(self):
        print("This is a manager")

manager = Manager()

manager.display_person()
manager.display_employee()
manager.display_manager()