import sqlite3

# Connect to SQLite3 database (creates file if not exists)
conn = sqlite3.connect('example.db')
cursor = conn.cursor()

# Create a table
cursor.execute('''
    CREATE TABLE IF NOT EXISTS students (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT,
        age INTEGER
    )
''')

# Insert data
cursor.execute("INSERT INTO students (name, age) VALUES (?, ?)", ("Aadi", 22))
cursor.execute("INSERT INTO students (name, age) VALUES (?, ?)", ("Tops", 25))
conn.commit()

# Fetch data
cursor.execute("SELECT * FROM students")
rows = cursor.fetchall()
for row in rows:
    print(row)

# Close