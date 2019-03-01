from tkinter import *

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

# Buttons


gui.mainloop()
