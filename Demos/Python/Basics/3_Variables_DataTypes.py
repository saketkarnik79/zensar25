name = "James Bond"
age = 40
salary = 100000.50
city = "London"
temperature = -25.5
count = 0
first_name = "James"
second_name = "Bond"
name = first_name + " " + second_name
print("Full Name:", name)

print("Name:", name)
print("Type of name:", type(name))
print("Age:", age)
print("Type of age:", type(age))
print("Salary:", salary)
print("Type of salary:", type(salary))
print("City:", city)
print("Type of city:", type(city))

print ("Hello " * 3)
print("Length of Full Name: ", len(name))
print("First character of Full Name: ", name[0])

isActive = True
print("Is Active:", isActive)
print("Type of isActive:", type(isActive))

isMarried = False
print("Is Married:", isMarried)
print("Type of isMarried:", type(isMarried))

isAdult = age >= 18
print("Is Adult:", isAdult)
print("Type of isAdult:", type(isAdult))

experience = None
if experience is None:
    print("Experience is not defined")
else:
    print("Experience:", experience)
print("Type of experience:", type(experience))
