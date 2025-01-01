import sqlite3


def connect():
    con = sqlite3.connect("Books.db")
    curs = con.cursor()
    curs.execute("CREATE TABLE IF NOT EXISTS book (id INTEGER PRIMARY KEY , title text , author text, year INTEGER, isbn INTEGER)")
    con.commit()
    con.close()
    
def insert(title, author , year, isbn):
    con = sqlite3.connect("books.db")
    curs = con.cursor()
    curs.execute("INSERT INTO book VALUES(NULL,?,?,?,?)", (title, author, year, isbn))
    con.commit()
    con.close()

def view ():
    con = sqlite3.connect("books.db")
    curs = con.cursor()
    curs.execute("SELECT * FROM book")
    rows = curs.fetchall()
    con.close()
    return rows

def search (title="", author="", year="", isbn=""):
    con = sqlite3.connect("books.db")
    curs = con.cursor()
    curs.execute("SELECT * FROM book WHERE title=? OR author=? OR year=? OR isbn=?", (title, author, year, isbn))
    rows = curs.fetchall()
    con.close()
    return rows

def delete (id):
    con = sqlite3.connect("books.db")
    curs = con.cursor()
    curs.execute("DELETE FROM book WHERE id=?", (id,))
    con.commit()
    con.close()

def update (id, title, author , year, isbn):
    con = sqlite3.connect("books.db")
    curs = con.cursor()
    curs.execute("UPDATE book SET title=?, author=?, year=?,isbn=? WHERE id=?", (title, author, year, isbn,id) )
    con.commit()
    con.close()
    
connect()

    