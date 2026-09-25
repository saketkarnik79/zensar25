class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    # def __str__(self):
    #     return f"Student: {self.name}, Age: {self.age}"

    def __repr__(self):
        return f"Student(name='{self.name}', age={self.age})"

student = Student("Rahul", 20)
print(student)