import sqlite3

conn = sqlite3.connect("employee.db")
cursor = conn.cursor()

emp_id = 102

cursor.execute(
    "SELECT * FROM Employee WHERE id = ?",
    (emp_id,)
)

employee = cursor.fetchone()

if employee:
    print("Employee Found:")
    print(employee)
else:
    print("Employee not found.")

conn.close()