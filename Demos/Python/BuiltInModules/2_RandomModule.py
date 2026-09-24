import random
import string

#number = random.randint(1, 100)
#number = random.random()
# number = random.uniform(20, 35)
# print(f"Random Number: {number}")

# students = [
#     "James",
#     "Steve",
#     "Alice",
#     "Matthew",
#     "Adam",
# ]

# student = random.choice(students)
# print(f"Selected student: {student}")

# string = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
# char = random.choice(string)
# print(f"Selected Character: {char}")

# students = [
#     "James",
#     "Steve",
#     "Alice",
#     "Matthew",
#     "Adam",
# ]

# selected_students = random.sample(students, 3)
# print(selected_students)

chars = string.ascii_letters + string.digits + string.punctuation
result = ""
for i in range(8):
    result += random.choice(chars)
print (result)