try:
    file = open("5_KeyError.py", "w")
    file.write("Hello Python")
    file.close()

except PermissionError:
    print("Error: You do not have permission to access this file.")