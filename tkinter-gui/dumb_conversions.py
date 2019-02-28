from tkinter import *
import re

conversions = [
                [1, 1.60934, 0.44704],
                [0.62137, 1, 0.27778],
                [2.23694, 3.6, 1],
              ]

# The "is this only numbers" pattern
num_patt = re.compile(r"^\d*\.?\d*$")

# I'm putting the callback function up here. Come and stop me!
def convert():

    def inserts(mph, kmh, mps):
            mph_t.insert(END, mph)
            kmh_t.insert(END, kmh)
            mps_t.insert(END, mps)

    mph = mph_t.get(1.0, END).strip()
    kmh = kmh_t.get(1.0, END).strip()
    mps = mps_t.get(1.0, END).strip()

    # Clear the boxes.
    mph_t.delete(1.0, END)
    kmh_t.delete(1.0, END)
    mps_t.delete(1.0, END)

    if mph and num_patt.fullmatch(mph):
        inserts(mph, float(mph)*conversions[0][1], float(mph)*conversions[0][2])
    elif kmh and num_patt.fullmatch(kmh):
        inserts(float(kmh)*conversions[1][0], kmh, float(kmh)*conversions[1][2])
    elif mps and num_patt.fullmatch(mps):
        inserts(float(mps)*conversions[2][0], float(mps)*conversions[2][1], mps)


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
