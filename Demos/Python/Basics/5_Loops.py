# Without Loops display 5 times "Hello World!"
# print("Hello World!")
# print("Hello World!")
# print("Hello World!")
# print("Hello World!")
# print("Hello World!")

# With Loops display 5 times "Hello World!"
# for i in range(5):  
#     print("Hello World!")
#     print("Value of i is: ", i)

# choice = "Y"
# while choice == "Y":
#     print("Hello World!")
#     choice = input("Do you want to continue? (Y/N): ").upper()

# for loop with start and end values
# for i in range(1, 6):  # Start from 1 to 5 (exclusive of 6)
#     print("Hello World!")

# for loop with start and end values and step value
# for i in range(1, 11, 2):  # Start from
#  1 to 10 (exclusive of 11) with a step of 2
# for i in range(2, 11, 4):
#     print("Hello World!")

# name = "Python"
# # for loop with string
# for char in name:
#     print(char)

# for loop with list
# fruits = ["Apple", "Banana", "Cherry"]
# for fruit in fruits:
#     print(fruit)

# multiplication table of given number using for loop
# number = int(input("Enter a number: "))
# for i in range(1, 11):
#     print(f"{number} x {i} = {number * i}")

# display pyramid of * using nested for loop
# rows = 5
# for i in range(rows, 0, -1):
#     for j in range(1, i + 1):
#         print("*", end=" ")
#     print()  # Move to the next line after each row

# infinite loop using while
# number = 1

# while number <= 5:
#     print(number)
#     number += 1  # Increment the number to avoid infinite loop

# example for break statement in loop
# for i in range(1, 11):
#     if i == 6:
#         break  # Exit the loop when i is 6
#     print(i)

# example for continue statement in loop
# for i in range(1, 11):
#     if i % 2 == 0:
#         continue  # Skip the even numbers
#     print(i)  # This will print only odd numbers

# example for pass statement in loop
for i in range(1, 11):
    if i % 2 == 0:
        pass  # Do nothing for even numbers
    else:
        print(i)  # This will print only odd numbers