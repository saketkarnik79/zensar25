# file = open("students.txt", "r")
# content = file.read()
# print(content)
# file.close()

# read line by line
file = open("students.txt", "r")
for line in file:
    print(line.strip())
file.close()