import sqlite3

conn = sqlite3.connect("employee.db")
cursor = conn.cursor()

cursor.execute(
    "INSERT INTO Employee VALUES (?, ?, ?, ?)",
    (101, "Rahul", "IT", 50000)
)

cursor.execute(
    "INSERT INTO Employee VALUES (?, ?, ?, ?)",
    (102, "Priya", "HR", 45000)
)

cursor.execute(
    "INSERT INTO Employee VALUES (?, ?, ?, ?)",
    (103, "Amit", "Sales", 55000)
)

conn.commit()

print("Records inserted successfully.")

conn.close()