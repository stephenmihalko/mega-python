import sqlite3
# id, title, author, year, isbn

# Connect and create the table
def connect():
    conn = sqlite3.connect("books_db.db")
    cur = conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS Books (id INTEGER PRIMARY KEY, title VARCHAR(100) NOT NULL, author VARCHAR(50) NOT NULL, year INTEGER, isbn VARCHAR(17) NOT NULL")
    conn.commit()
    conn.close()

# View all
def view_all():
    conn = sqlite3.connect("books_db.db")
    cur = conn.cursor()
    cur.execute("SELECT * FROM Books")
    rows = cur.fetchall()
    conn.close()
    return rows
    
# Search for record
def search(title="", author="", year="", isbn=""):
    conn = sqlite3.connect("books_db.db")
    cur = conn.cursor()
    cur.execute("SELECT title, author, year, isbn FROM Books WHERE title=? OR author=? OR year=? OR isbn=?", (title, author, year, isbn))
    rows = cur.fetchall()
    conn.close()
    return rows
    
# Add record
def insert(title, author, year, isbn):
    conn = sqlite3.connect("books_db.db")
    cur = conn.cursor()
    cur.execute("INSERT INTO Books VALUES (NULL, ?, ?, ?, ?)", (title, author, year, isbn))
    conn.commit()
    conn.close()
    
# Update record
def update(id, title, author, year, isbn):
    conn = sqlite3.connect("books_db.db")
    cur = conn.cursor()
    cur.execute("UPDATE Books SET title=?, author=?, year=?, isbn=? WHERE id = ?", (title, author, year, isbn, id))
    conn.commit()
    conn.close()
    
# Delete record
def delete(id):
    conn = sqlite3.connect("books_db.db")
    cur = conn.cursor()
    # We can get away with using only ID because the UI requires the user to select a book from the list and this has the ID.
    cur.execute("DELETE FROM Books WHERE id = ?", (id,))
    conn.commit()
    conn.close()
