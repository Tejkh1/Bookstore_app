import sqlite3


def connect():
    con = sqlite3.connect("bookstore.db")
    cur = con.cursor()
    cur.execute("""
        CREATE TABLE IF NOT EXISTS books (
            id INTEGER PRIMARY KEY,
            title TEXT NOT NULL,
            author TEXT NOT NULL,
            year INTEGER,
            isbn TEXT
        )
    """)
    con.commit()  # commit the changes to the database
    con.close()  # closes the database

def insertbook(title, author, year, isbn):
    con = sqlite3.connect("bookstore.db")
    cur = con.cursor()
    cur.execute("INSERT INTO books (title, author, year, isbn) VALUES (?, ?, ?, ?)",
                (title, author, year, isbn))
    con.commit()
    con.close()

def viewstore():
    conn = sqlite3.connect("bookstore.db")
    cur = conn.cursor()
    cur.execute("SELECT * FROM bookstore")
    rows = cur.fetchall()
    conn.close
    return rows

