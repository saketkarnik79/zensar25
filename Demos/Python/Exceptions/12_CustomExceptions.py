import InvalidMarksError as iem

try:
    marks = int(input("Enter marks: "))

    if marks < 0 or marks > 100:
        raise iem.InvalidMarksError("Marks must be between 0 and 100.")

except iem.InvalidMarksError as e:
    print( e)
else:
     print("Marks:", marks)