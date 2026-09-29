# Basic Generator using yield
# def generate_numbers():
#     yield 10
#     yield 20
#     yield 30

# generator = generate_numbers()

# print(next(generator))
# print(next(generator))
# print(next(generator))

# # Generator with a Loop
# def generate_numbers(limit):
#     for number in range(1, limit + 1):
#         yield number

# for number in generate_numbers(5):
#     print(number)

# # Generator for Even Numbers
# def even_numbers(limit):
#     for number in range(1, limit + 1):
#         if number % 2 == 0:
#             yield number

# for number in even_numbers(10):
#     print(number)

# # Generator for Squares
# def generate_squares(limit):
#     for number in range(1, limit + 1):
#         yield number * number

# for square in generate_squares(5):
#     print(square)

# Generator Expression
# squares = (number * number for number in range(1, 6))

# print(next(squares))
# print(next(squares))
# print(next(squares))

# Employee Generator
def get_employees():
    employees = [
        {"id": 101, "name": "Amit"},
        {"id": 102, "name": "Neha"},
        {"id": 103, "name": "Rahul"}
    ]

    for employee in employees:
        yield employee


for employee in get_employees():
    print(employee["id"], employee["name"])