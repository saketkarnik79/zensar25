import sqlite3

# Connect to database
conn = sqlite3.connect("employee.db")

# Create cursor
cursor = conn.cursor()

# Create Employee table
cursor.execute("""
CREATE TABLE IF NOT EXISTS Employee (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    department TEXT,
    salary REAL
)
""")

conn.commit()

print("Employee table created successfully.")

conn.close()