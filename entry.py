from tkinter import *

# EVERYTHING IS A WIDGET

root = Tk()

e = Entry(root, width=40)
e.pack()
e.get()
e.insert(0, "Enter Your Name. You Won't.")

def myClick():
	myLabel = Label(root, text=e.get() + " sucks balls")
	myLabel.pack()

myButton = Button(root, text="You're Scared to Click this box. I know it."
	, padx=25, pady=25, command=myClick, fg="black", bg="yellow")
myButton.pack()

root.mainloop()
















