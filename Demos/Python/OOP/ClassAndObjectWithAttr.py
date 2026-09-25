# Custom class
class Student:
    school = "XYZ School" # Class attribute

    def __init__(self, name, age):
        self.name = name    # Object attribute
        self.age = age # Object attribute

    def display(self):
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"School: {Student.school}")

stud1 = Student("Rahul", 20)
stud2 = Student("Priya", 21)
stud1.display()
print()
stud2.display()