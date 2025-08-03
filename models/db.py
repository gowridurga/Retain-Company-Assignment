# models/db.py

import sqlite3

def get_db_connection():
    conn = sqlite3.connect("users.db", check_same_thread=False)
    conn.row_factory = sqlite3.Row  # ✅ Very Important!
    return conn
