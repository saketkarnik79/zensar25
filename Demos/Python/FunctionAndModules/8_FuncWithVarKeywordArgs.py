def display_student(**details):
    for key, value in details.items():
        print(f"{key}: {value}")

# example usage
display_student(name="James", age=25, course="Python", city="New york")