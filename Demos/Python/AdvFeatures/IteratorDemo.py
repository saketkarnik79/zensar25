# Basic Iterator
# numbers = [10, 20, 30, 40, 50]

# iterator = iter(numbers)

# print(next(iterator))
# print(next(iterator))
# print(next(iterator))
# print(next(iterator))
# print(next(iterator))
# print(next(iterator))

# Iterator with a for loop
# fruits = ["Apple", "Mango", "Orange", "Banana"]

# for fruit in fruits:
#     print(fruit)

# Handling StopIteration exception
numbers = [10, 20, 30]

iterator = iter(numbers)

while True:
    try:
        value = next(iterator)
        print(value)
    except StopIteration:
        print("No more values.")
        break