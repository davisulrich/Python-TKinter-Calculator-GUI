from tkinter import *

# EVERYTHING IS A WIDGET

root = Tk()

def myClick():
	myLabel = Label(root, text="You clicked it!")
	myLabel.pack()

myButton = Button(root, text="Click Me! You won't!", padx=25, pady=25
	, command=myClick, fg="black", bg="yellow")
myButton.pack()

root.mainloop()
















