from tkinter import *

# EVERYTHING IS A WIDGET

root = Tk()

# Creating a label widget
myLabel1 = Label(root, text="Hello World!")
myLabel2= Label(root, text="It's Friyay!")

# slapping it on the screen
myLabel1.grid(row=0, column=0)
myLabel2.grid(row=1, column=1)

root.mainloop()
















