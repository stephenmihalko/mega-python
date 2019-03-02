from tkinter import *
from OO_backend import BooksBackend

# This is part of the "main method"
backend = BooksBackend()

# The class definition
class BooksFrontend:

    def __init__(self, window):

        self.row = (-1,)

        self.gui = window

        self.gui.wm_title("Bookstore")

        # Static labels
        Label(self.gui, text="Title").grid(row=0, column=0)
        Label(self.gui, text="Author").grid(row=0, column=2)
        Label(self.gui, text="Year").grid(row=1, column=0)
        Label(self.gui, text="ISBN").grid(row=1, column=2)

        # Entry boxes
        self.title_e = Entry(self.gui, width=15)
        self.title_e.grid(row=0, column=1)
        
        self.author_e = Entry(self.gui, width=15)
        self.author_e.grid(row=0, column=3)
        
        self.year_e = Entry(self.gui, width=15)
        self.year_e.grid(row=1, column=1)
        
        self.isbn_e = Entry(self.gui, width=15)
        self.isbn_e.grid(row=1, column=3)

        # Listbox
        self.lb = Listbox(self.gui, width=20)
        self.lb.grid(row=2, column=0, rowspan=6, columnspan=2)

        # Scrollbar
        self.sb = Scrollbar(self.gui)
        self.sb.grid(row=2, column=2, rowspan=6)

        # Link listbox and scrollbar
        self.lb.configure(yscrollcommand=self.sb.set)
        self.sb.configure(command=self.lb.yview)

        # This tells the Listbox to call get_selected_row when something is selected in it.
        self.lb.bind("<<ListboxSelect>>", self.get_selected_row)

        # Buttons
        buttonwidth = 10
        Button(self.gui, text="View all", width=buttonwidth, command=self.view).grid(row=2, column=3)
        Button(self.gui, text="Search entry", width=buttonwidth, command=self.search).grid(row=3, column=3)
        Button(self.gui, text="Add entry", width=buttonwidth, command=self.insert).grid(row=4, column=3)
        Button(self.gui, text="Update entry", width=buttonwidth, command=self.update).grid(row=5, column=3)
        Button(self.gui, text="Delete entry", width=buttonwidth, command=self.delete).grid(row=6, column=3)
        Button(self.gui, text="Close", width=buttonwidth, command=self.gui.destroy).grid(row=7, column=3)

    # This parameter has information about the event
    def get_selected_row(self, event):
        if len(self.lb.curselection()) > 0:
            # This gives back a tuple, but we only want the first number (the row)
            index = self.lb.curselection()[0]
            self.row = self.lb.get(index)

            # Clear the entry boxes and add the information from the thing you just clicked
            self.clear_entries()
            self.title_e.insert(END, self.row[1])
            self.author_e.insert(END, self.row[2])
            self.year_e.insert(END, self.row[3])
            self.isbn_e.insert(END, self.row[4])

    def clear_entries(self):
        self.title_e.delete(0, END)
        self.author_e.delete(0, END)
        self.year_e.delete(0, END)
        self.isbn_e.delete(0, END)

    def view(self):
        self.lb.delete(0, END)
        for theRow in backend.view_all():
            self.lb.insert(END, theRow)

    # We need to use these wrappers because we're not allowed to use inputs in the command=? part
    def search(self):
        self.lb.delete(0, END)
        for theRow in backend.search(self.title_e.get(), self.author_e.get(), self.year_e.get(), self.isbn_e.get()):
            self.lb.insert(END, theRow)
        
    def insert(self):
        backend.insert(self.title_e.get(), self.author_e.get(), self.year_e.get(), self.isbn_e.get())
        self.view()

    def update(self):
        if len(self.row) > 1:
            backend.update(self.row[0], self.title_e.get(), self.author_e.get(), self.year_e.get(), self.isbn_e.get())
            self.view()

    def delete(self):
        if len(self.row) > 1:
            # The tuple you get from "row" in get_selected_row() starts with the ID
            backend.delete(self.row[0])
            self.view()
            self.clear_entries()



    

# The remainder of the "main method"
gui = Tk()
BooksFrontend(gui)
gui.mainloop()
