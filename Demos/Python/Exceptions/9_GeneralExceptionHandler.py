try:
    number = int(input("Enter a number: "))
    result = 100 / number
    print(result)

except Exception as e:
    print("An error occurred:", e)