import sqlite3

conn = sqlite3.connect("employee.db")
cursor = conn.cursor()

cursor.execute(
    "UPDATE Employee SET salary = ? WHERE id = ?",
    (50000, 102)
)

conn.commit()

print("Employee salary updated successfully.")

conn.close()