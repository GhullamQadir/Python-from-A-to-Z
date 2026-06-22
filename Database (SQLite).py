import sqlite3

# Connect to database (creates if not exists)
conn = sqlite3.connect("my_database.db")
cursor = conn.cursor()

# Create table
cursor.execute("""
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        email TEXT UNIQUE,
        age INTEGER
    )
""")

# Insert data
cursor.execute("INSERT INTO users (name, email, age) VALUES (?, ?, ?)",
               ("Alice", "alice@example.com", 25))
conn.commit()

# Query data
cursor.execute("SELECT * FROM users")
rows = cursor.fetchall()
for row in rows:
    print(row)

# Update
cursor.execute("UPDATE users SET age = ? WHERE name = ?", (29, "Aftab"))

# Delete
cursor.execute("DELETE FROM users WHERE id = ?", (1,))

# Parameterized queries (prevents SQL injection)
name = "Henry"
cursor.execute("SELECT * FROM users WHERE name = ?", (name,))

# Close connection
conn.close()

# Context manager (recommended)
with sqlite3.connect("my_database.db") as conn:
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM users")
    print(cursor.fetchall())
