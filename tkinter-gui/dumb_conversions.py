import tkinter as tk
import re

# I'm putting the callback function up here. Come and stop me!
def convert():
	

# The "is this only numbers" pattern
num_patt = re.compile(r"^\d+$")

# Create a new window
win = tk.Tk()

# Create a button that calls the convert function.
go_button = tk.Button(win, text="Go!", command=convert)

# This is a box with a static message.
msg = Message(window, text="Enter speed in mph here:", height=1, width=20)
