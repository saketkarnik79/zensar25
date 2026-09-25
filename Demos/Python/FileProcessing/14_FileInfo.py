import os

filename = "students.txt"

if os.path.exists(filename):

    print("File exists")
    print("File size:", os.path.getsize(filename), "bytes")

else:
    print("File does not exist")