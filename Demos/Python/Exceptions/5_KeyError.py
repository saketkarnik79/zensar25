try:
    student = {
        "name": "Rahul",
        "age": 20
    }

    print(student["marks"])

except KeyError:
    print("Error: The requested key does not exist.")