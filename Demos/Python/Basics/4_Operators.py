# Comparison Operators
# Comparison operators are used to compare two values. 
# They return a boolean value (True or False)

# == operator checks if two values are equal
a = 10
b = 10
c = (a == b)  # This will be True
print("a == b:", c)

# != operator checks if two values are not equal
d = (a != b)  # This will be False
print("a != b:", d)

# < operator checks if the first value is less than the second value
e = (a < b)  # This will be False
print("a < b:", e)

# > operator checks if the first value is greater than the second value
f = (a > b)  # This will be False
print("a > b:", f)

# <= operator checks if the first value is less than or equal to the second value
g = (a <= b)  # This will be True
print("a <= b:", g)

# >= operator checks if the first value is greater than or equal to the second value
h = (a >= b)  # This will be True
print("a >= b:", h)

# Logical Operators
# Logical operators are used to combine conditional statements.
# and operator returns True if both statements are true
age = 25
salary = 50000
if age >= 18 and salary >= 30000:
    print("Eligible for loan")
else:
    print("Not eligible for loan")

# or operator returns True if one of the statements is true
if age >= 18 or salary >= 60000:
    print("Satisfied at least one condition")
else:
    print("Not satisfied any condition")

# not operator reverses the result, 
# returns False if the result is true

is_logged_in = True
print(not is_logged_in)  # This will print False

is_admin = False
if not is_admin:
    print("Access denied")

# combining logical operators
if age >= 18 and (salary >= 30000 or is_admin):
    print("Eligible for loan")
else:
    print("Not eligible for loan")

# Assignment Operators
# Assignment operators are used to assign values to variables.
x = 5 # Basic assignment operator
print("Initial value of x:", x)
x += 3  # This is addition assignment operator equivalent to x = x + 3
print("After x += 3:", x)
x -= 2  # This is subtraction assignment operator equivalent to x = x - 2
print("After x -= 2:", x)
x *= 4  # This is multiplication assignment operator equivalent to x = x * 4
print("After x *= 4:", x)
x /= 2  # This is division assignment operator equivalent to x = x / 2
print("After x /= 2:", x)
x %= 3  # This is modulus assignment operator equivalent to x = x % 3
print("After x %= 3:", x)
x **= 2  # This is exponentiation assignment operator equivalent to x = x ** 2
print("After x **= 2:", x)
x//= 2  # This is floor division assignment operator equivalent to x = x // 2
print("After x //= 2:", x)

# Membership Operators
# Membership operators are used to test if a sequence is presented an object.
fruits = ["apple", "banana", "cherry"]
print("apple" in fruits)  # This will print True
print("mango" not in fruits)  # This will print True

message = "Hello, welcome to the world of Python!"
print("Python" in message)  # This will print True
print("Java" not in message)  # This will print True

# Identity Operators
# Identity operators are used to compare the memory locations of two objects.
a = 5
b = 5
c = 10
print(a is b)  # This will print True
print(a is c)  # This will print False
print(a is not c)  # This will print True

a=[1, 2, 3]
b=[1, 2, 3]
print(a is b)  # This will print False because they are different objects in memory
print(a == b)  # This will print True because they have the same content

value = None
if value is None:
    print("Value is None") # This will print "Value is None"
value = "Python"
if value is not None:
    print("Value is available") # This will print "Value is available"