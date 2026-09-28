import sqlite3

conn = sqlite3.connect("employee.db")
cursor = conn.cursor()

cursor.execute(
    "DELETE FROM Employee WHERE id = ?",
    (103,)
)

conn.commit()

print("Employee deleted successfully.")

conn.close()