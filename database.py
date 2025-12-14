import sqlite3
from datetime import datetime

def connect_db():
    conn = sqlite3.connect("bmi_data.db")
    cursor = conn.cursor()
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS bmi_data (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT,
        weight REAL,
        height REAL,
        bmi REAL,
        date TEXT
    )
    """)
    conn.commit()
    return conn


def insert_data(conn, name, weight, height, bmi):
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO bmi_data (name, weight, height, bmi, date) VALUES (?, ?, ?, ?, ?)",
        (name, weight, height, bmi, datetime.now().strftime("%Y-%m-%d"))
    )
    conn.commit()


def fetch_user_data(conn, name):
    cursor = conn.cursor()
    cursor.execute("SELECT date, bmi FROM bmi_data WHERE name=?", (name,))
    return cursor.fetchall()
