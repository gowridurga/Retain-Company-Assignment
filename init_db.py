import sqlite3
from werkzeug.security import generate_password_hash

# Connect to DB
conn = sqlite3.connect('users.db')
cursor = conn.cursor()

# Create table
cursor.execute('''
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    email TEXT NOT NULL UNIQUE,
    password TEXT NOT NULL
)
''')

# Clear old data if any
cursor.execute("DELETE FROM users")

# Insert hashed users
users = [
    ("John Doe", "john@example.com", generate_password_hash("password123")),
    ("Jane Smith", "jane@example.com", generate_password_hash("secret456")),
    ("Bob Johnson", "bob@example.com", generate_password_hash("qwerty789")),
    ("Test User", "test@example.com", generate_password_hash("testpass123"))  # 👈 Add this for login testing
]

cursor.executemany("INSERT INTO users (name, email, password) VALUES (?, ?, ?)", users)

conn.commit()
conn.close()
print("✅ Database initialized with hashed passwords")
