from tkinter import *

gui = Tk()

# Static labels
Label(gui, text="Title").grid(row=0, column=0)
Label(gui, text="Author").grid(row=0, column=2)
Label(gui, text="Year").grid(row=2, column=0)
Label(gui, text="ISBN").grid(row=2, column=2)

# Entry boxes
title_e = Entry(gui)
title_e.grid(row=0, column=1)

author_e = Entry(gui)
author_e.grid(row=0, column=3)

year_e = Entry(gui)
year_e.grid(row=2, column=1)

isbn_e = Entry(gui)
isbn_e.grid(row=2, column=3)

# Listbox

# Scrollbar

# Buttons


gui.mainloop()
