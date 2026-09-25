try:
    age = int(input("Enter your age: "))
    print(f"Age: {age}")

except ValueError:
    print("Error: Please enter a valid number.")