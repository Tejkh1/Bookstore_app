import sqlite3


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
