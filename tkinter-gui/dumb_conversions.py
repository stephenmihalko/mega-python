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

msg_ht = 1
msg_wd = 25

# These are boxes with static messages.
mph_msg = Message(win, text="miles per hour", height=msg_ht, width=msg_wd)
kmh_msg = Message(win, text="kilometers per hour", height=msg_ht, width=msg_wd)
mps_msg = Message(win, text="meters per second", height=msg_ht, width=msg_wd)
fpf_msg = Message(win, text="furlongs per fortnight", height=msg_ht, width=msg_wd)




