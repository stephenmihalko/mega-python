# This is better than import tkinter because it puts us in the tkinter namespace.
from tkinter import *

# Create an empty window.
window = Tk()

# This is a callback function for when you press a button!
def mi_to_km():
	# Clear the text box - thanks stackoverflow!
	t1.delete(1.0, END)
	t1.insert(END, int(e1_val.get())/1.6)

# Create a button and tell it what window to go to
b1 = Button(window, text="Execute", command=mi_to_km)
# Put the button on the window better
b1.grid(row=0, column=0)

e1_val = StringVar()
# Create an entry box
e1 = Entry(window, textvariable=e1_val)
# Put the button on the window better
e1.grid(row=0, column=1)

# Create a text box
t1 = Text(window, height=1, width=20)
t1.grid(row=0, column=2)

# This is to keep the window going - otherwise it exits manually.
window.mainloop()
