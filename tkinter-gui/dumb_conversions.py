from tkinter import *
import re

conversions = [
                [1, 1.60934, 0.44704],
                [0.62137, 1, 0.27778],
                [2.23694, 3.6, 1],
              ]

# I'm putting the callback function up here. Come and stop me!
def convert():
    # Clear the boxes.
    mph_t.delete(1.0, END)
    kmh_t.delete(1.0, END)
    mps_t.delete(1.0, END)

    # If there's nothing there, then print error messages.
    if not mph_t.get("1.0", "end-1c") and not kmh_t.get("1.0", "end-1c") and not mps_t.get("1.0", "end-1c"):
        mph_t.insert(END, "No value!")
        kmh_t.insert(END, "No value!")
        mps_t.insert(END, "No value!")
	

# The "is this only numbers" pattern
num_patt = re.compile(r"^\d+$")

# Create a new window
win = Tk()

# Create a button that calls the convert function.
Button(win, text="Go!", command=convert).grid(row=3, column=1)

ht = 1
wd = 10

# These are boxes with static messages.
Label(win, text="mph").grid(row=0, column=1, sticky='w')
Label(win, text="km/h").grid(row=1, column=1, sticky='w')
Label(win, text="m/s").grid(row=2, column=1, sticky='w')

# The entry boxes
mph_t = Text(win, height=ht, width=wd)
kmh_t = Text(win, height=ht, width=wd)
mps_t = Text(win, height=ht, width=wd)

mph_t.grid(row=0, column=0)
kmh_t.grid(row=1, column=0)
mps_t.grid(row=2, column=0)


win.mainloop()
