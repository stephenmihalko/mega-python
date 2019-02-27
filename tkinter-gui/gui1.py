# This is better than import tkinter because it puts us in the tkinter namespace.
from tkinter import *

# Create an empty window.
window = Tk()

# Create a button and tell it what window to go to
b1 = Button(window, text="Execute")
# Put the button on the window
b1.pack()


# This is to keep the window going - otherwise it exits manually.
window.mainloop()
