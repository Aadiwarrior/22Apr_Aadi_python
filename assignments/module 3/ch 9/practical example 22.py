import sqlite3

conn = sqlite3.connect('example.db')
cursor = conn.cursor()

cursor.execute('''
    CREATE TABLE IF NOT EXISTS students (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT,
        age INTEGER
    )
''')

cursor.execute("INSERT INTO students (name, age) VALUES (?, ?)", ("Aadi", 22))
cursor.execute("INSERT INTO students (name, age) VALUES (?, ?)", ("Tops", 25))
conn.commit()

cursor.execute("SELECT * FROM students")
rows = cursor.fetchall()
print(rows)

