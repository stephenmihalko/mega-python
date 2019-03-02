from tkinter import *
from OO_backend import BooksBackend

class BooksFrontend:

    row = (-1,)

    def __init__(self):

        self.gui = Tk()

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

    # This parameter has information about the event
    def get_selected_row(event):
        global row
        if len(lb.curselection()) > 0:
            # This gives back a tuple, but we only want the first number (the row)
            index = lb.curselection()[0]
            row = lb.get(index)

            # Clear the entry boxes and add the information from the thing you just clicked
            clear_entries()
            title_e.insert(END, row[1])
            author_e.insert(END, row[2])
            year_e.insert(END, row[3])
            isbn_e.insert(END, row[4])

    def clear_entries():
        title_e.delete(0, END)
        author_e.delete(0, END)
        year_e.delete(0, END)
        isbn_e.delete(0, END)

    def view():
        lb.delete(0, END)
        for row in backend.view_all():
            lb.insert(END, row)

    # We need to use these wrappers because we're not allowed to use inputs in the command=? part
    def search():
        lb.delete(0, END)
        for row in backend.search(title_e.get(), author_e.get(), year_e.get(), isbn_e.get()):
            lb.insert(END, row)
        
    def insert():
        backend.insert(title_e.get(), author_e.get(), year_e.get(), isbn_e.get())
        view()

    def update():
        if len(row) > 1:
            backend.update(row[0], title_e.get(), author_e.get(), year_e.get(), isbn_e.get())
            view()

    def delete():
        if len(row) > 1:
            # The tuple you get from "row" in get_selected_row() starts with the ID
            backend.delete(row[0])
            view()
            clear_entries()



    

    # Listbox
    lb = Listbox(gui, width=20)
    lb.grid(row=2, column=0, rowspan=6, columnspan=2)

    # Scrollbar
    sb = Scrollbar(gui)
    sb.grid(row=2, column=2, rowspan=6)

    # Link listbox and scrollbar
    lb.configure(yscrollcommand=sb.set)
    sb.configure(command=lb.yview)

    # This tells the Listbox to call get_selected_row when something is selected in it.
    lb.bind("<<ListboxSelect>>", get_selected_row)

    # Buttons
    buttonwidth = 10
    Button(gui, text="View all", width=buttonwidth, command=view).grid(row=2, column=3)
    Button(gui, text="Search entry", width=buttonwidth, command=search).grid(row=3, column=3)
    Button(gui, text="Add entry", width=buttonwidth, command=insert).grid(row=4, column=3)
    Button(gui, text="Update entry", width=buttonwidth, command=update).grid(row=5, column=3)
    Button(gui, text="Delete entry", width=buttonwidth, command=delete).grid(row=6, column=3)
    Button(gui, text="Close", width=buttonwidth, command=gui.destroy).grid(row=7, column=3)

    gui.mainloop()
