# Currency Converter

print("===== Currency Converter =====")
print("1. USD to INR")
print("2. INR to USD")
print("3. EUR to INR")
print("4. INR to EUR")
print("5. GBP to INR")
print("6. INR to GBP")

choice = input("Enter your choice (1-6): ")

amount = float(input("Enter amount: "))

# Sample exchange rates
USD_TO_INR = 85.00
EUR_TO_INR = 98.00
GBP_TO_INR = 115.00

if choice == "1":
    result = amount * USD_TO_INR
    print("Amount in INR:", result)

elif choice == "2":
    result = amount / USD_TO_INR
    print("Amount in USD:", result)

elif choice == "3":
    result = amount * EUR_TO_INR
    print("Amount in INR:", result)

elif choice == "4":
    result = amount / EUR_TO_INR
    print("Amount in EUR:", result)

elif choice == "5":
    result = amount * GBP_TO_INR
    print("Amount in INR:", result)

elif choice == "6":
    result = amount / GBP_TO_INR
    print("Amount in GBP:", result)

else:
    print("Invalid choice")