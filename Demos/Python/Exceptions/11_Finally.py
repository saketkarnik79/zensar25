try:
    file = open(input("Name of file: "), "r")
    content = file.read()
    print(content)

except FileNotFoundError:
    print("File not found.")

finally:
    print("File processing operation completed.")