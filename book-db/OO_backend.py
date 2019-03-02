import sqlite3
# id, title, author, year, isbn

class BooksBackend:

    # Connect and create the table in CONSTRUCTOR
    def __init__(self):
    
        # ---- INSTANCE VARIABLES ----
        self.conn = sqlite3.connect("books_db.db")
        self.cur = self.conn.cursor()

        self.cur.execute("CREATE TABLE IF NOT EXISTS Books (id INTEGER PRIMARY KEY, title VARCHAR(100) NOT NULL, author VARCHAR(50) NOT NULL, year INTEGER, isbn VARCHAR(17) NOT NULL)")
        self.commit()

    # View all
    def view_all(self):
        self.cur.execute("SELECT * FROM Books")
        rows = self.cur.fetchall()
        return rows
    
    # Search for record
    def search(self, title="", author="", year="", isbn=""):
        self.cur.execute("SELECT * FROM Books WHERE title=? OR author=? OR year=? OR isbn=?", (title, author, year, isbn))
        rows = self.cur.fetchall()
        return rows
    
    # Add record
    def insert(self, title, author, year, isbn):
        self.cur.execute("INSERT INTO Books VALUES (NULL, ?, ?, ?, ?)", (title, author, year, isbn))
        self.commit()
        
    # Update record
    def update(self, id, title, author, year, isbn):
        self.cur.execute("UPDATE Books SET title=?, author=?, year=?, isbn=? WHERE id = ?", (title, author, year, isbn, id))
        self.commit()
        
    # Delete record
    def delete(self, id):
        # We can get away with using only ID because the UI requires the user to select a book from the list and this has the ID.
        self.cur.execute("DELETE FROM Books WHERE id = ?", (id,))
        self.commit()

    # Commit changes
    def commit(self):
        self.conn.commit()

    # Close the connection to the database before we close.
    def __del__(self):
        self.conn.close()
    
