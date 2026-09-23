# Area Calculator

print("===== Area Calculator =====")
print("1. Circle")
print("2. Rectangle")
print("3. Square")
print("4. Triangle")

choice = input("Enter your choice (1-4): ")

if choice == "1":
    # Area of Circle
    radius = float(input("Enter radius: "))

    area = 3.14159 * radius * radius

    print("Area of Circle:", area)

elif choice == "2":
    # Area of Rectangle
    length = float(input("Enter length: "))
    width = float(input("Enter width: "))

    area = length * width

    print("Area of Rectangle:", area)

elif choice == "3":
    # Area of Square
    side = float(input("Enter side: "))

    area = side * side

    print("Area of Square:", area)

elif choice == "4":
    # Area of Triangle
    base = float(input("Enter base: "))
    height = float(input("Enter height: "))

    area = 0.5 * base * height

    print("Area of Triangle:", area)

else:
    print("Invalid choice")