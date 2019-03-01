import sqlite3
# id, title, author, year, isbn

# View all
def view_all():
    conn = sqlite3.connect("books_db.db")
    cur = conn.cursor()
    cur.execute("SELECT * FROM Books")
    rows = cur.fetchall()
    conn.close()
    return rows
    
# Search for record
def search():
    
# Add record
def add():
    
# Update record
def update():
    
# Delete record
def delete():
    
