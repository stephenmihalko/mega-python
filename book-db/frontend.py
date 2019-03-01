from tkinter import *
import backend

# This parameter has information about the event
def get_selected_row(event):
    # This gives back a tuple, but we only want the first number (the row)
    index = lb.curselection()[0]
    row = lb.get(index)
    # The tuple you get back from "row" starts with the ID
    backend.delete(row[0])

def view():
    lb.delete(0, END)
    for row in backend.view_all():
        lb.insert(END, " ".join(row))

# We need to use these wrappers because we're not allowed to use inputs in the command=? part
def search():
    lb.delete(0, END)
    for row in backend.search(title_e.get(), author_e.get(), year_e.get(), isbn_e.get()):
        lb.insert(END, " ".join(row))
    
def insert():
    backend.insert(title_e.get(), author_e.get(), year_e.get(), isbn_e.get())


gui = Tk()

# Static labels
Label(gui, text="Title").grid(row=0, column=0)
Label(gui, text="Author").grid(row=0, column=2)
Label(gui, text="Year").grid(row=1, column=0)
Label(gui, text="ISBN").grid(row=1, column=2)

# Entry boxes
title_e = Entry(gui, width=15)
title_e.grid(row=0, column=1)

author_e = Entry(gui, width=15)
author_e.grid(row=0, column=3)

year_e = Entry(gui, width=15)
year_e.grid(row=1, column=1)

isbn_e = Entry(gui, width=15)
isbn_e.grid(row=1, column=3)

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
Button(gui, text="Update entry", width=buttonwidth).grid(row=5, column=3)
Button(gui, text="Delete entry", width=buttonwidth).grid(row=6, column=3)
Button(gui, text="Close", width=buttonwidth).grid(row=7, column=3)

gui.mainloop()
