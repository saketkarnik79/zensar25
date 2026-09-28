import sqlite3

conn = sqlite3.connect("employee.db")
cursor = conn.cursor()

cursor.execute("SELECT * FROM Employee")

records = cursor.fetchall()

print("Employee Records:")

for employee in records:
    print(employee)

conn.close()