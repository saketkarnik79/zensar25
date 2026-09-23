# Simple Calculator

num1 = float(input("Enter first number: "))
operator = input("Enter operator (+, -, *, /, %, **, //): ")
num2 = float(input("Enter second number: "))

if operator == "+":
    result = num1 + num2

elif operator == "-":
    result = num1 - num2

elif operator == "*":
    result = num1 * num2

elif operator == "/":
    if num2 != 0:
        result = num1 / num2
    else:
        result = "Cannot divide by zero"

elif operator == "%":
    if num2 != 0:
        result = num1 % num2
    else:
        result = "Cannot perform modulo operation with zero"
elif operator == "**":
    result = num1 ** num2 # Exponentiation operator
elif operator == "//":
    if num2 != 0:
        result = num1 // num2 # Floor division operator
    else:
        result = "Cannot perform floor division with zero"
else:
    result = "Invalid operator"

print("Result:", result)