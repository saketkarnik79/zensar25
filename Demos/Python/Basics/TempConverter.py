# Temperature Converter

print("Temperature Converter")
print("1. Celsius to Fahrenheit")
print("2. Fahrenheit to Celsius")
print("3. Celsius to Kelvin")
print("4. Kelvin to Celsius")
print("5. Fahrenheit to Kelvin")
print("6. Kelvin to Fahrenheit")

choice = input("Enter your choice (1-6): ")

temperature = float(input("Enter temperature: "))

if choice == "1":
    # Celsius to Fahrenheit
    result = (temperature * 9 / 5) + 32
    print("Temperature in Fahrenheit:", result)

elif choice == "2":
    # Fahrenheit to Celsius
    result = (temperature - 32) * 5 / 9
    print("Temperature in Celsius:", result)

elif choice == "3":
    # Celsius to Kelvin
    result = temperature + 273.15
    print("Temperature in Kelvin:", result)

elif choice == "4":
    # Kelvin to Celsius
    result = temperature - 273.15
    print("Temperature in Celsius:", result)

elif choice == "5":
    # Fahrenheit to Kelvin
    result = (temperature - 32) * 5 / 9 + 273.15
    print("Temperature in Kelvin:", result)

elif choice == "6":
    # Kelvin to Fahrenheit
    result = (temperature - 273.15) * 9 / 5 + 32
    print("Temperature in Fahrenheit:", result)

else:
    print("Invalid choice")