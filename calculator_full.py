# Current video:
# https://www.youtube.com/watch?v=NoTM8JciWaQ

# Steve Jobs interview: https://www.youtube.com/watch?v=DbfejwP1d3c

# Command prompts:
# cd Documents/Python Scripts/Calculator GUI
# python calculator_full.py

from tkinter import *
import tkinter.font as font

root = Tk()
root.title("Best Calculator Ever")
root.iconbitmap(r"C:/Users/davis.ulrich/Documents/Python Scripts/Calculator GUI/alien.ico")

e = Entry(root, font = "Helvetica 32", bg="#c9c9c9", width=12, borderwidth=5)
e.grid(row=0, column=0, columnspan=3, padx=10, pady=10)

def button_click(number):
	current_num = str(e.get())
	e.delete(0, END)
	e.insert(0, current_num + str(number))

def clear_entry():
	e.delete(0, END)

def save(operator):
	# the first number of the operation
	first_num = e.get()
	global f_num
	f_num = int(first_num)

	# the operator (string)
	global math_operator
	math_operator = operator

	# delete number in the box
	e.delete(0, END)

def equals():
	second_num = e.get()
	e.delete(0, END)

	if math_operator == "plus":
		e.insert(0, f_num + int(second_num))
	elif math_operator == "subtract":
		e.insert(0, f_num - int(second_num))
	elif math_operator == "multiply":
		e.insert(0, f_num * int(second_num))
	elif math_operator == "divide":
		e.insert(0, int(f_num / int(second_num)))

# define butons
button_1 = Button(root, text="1", padx=40, pady=20, command=lambda: button_click(1), bg="#93f0f5")
button_2 = Button(root, text="2", padx=40, pady=20, command=lambda: button_click(2), bg="#93f0f5")
button_3 = Button(root, text="3", padx=40, pady=20, command=lambda: button_click(3), bg="#93f0f5")
button_4 = Button(root, text="4", padx=40, pady=20, command=lambda: button_click(4), bg="#93f0f5")
button_5 = Button(root, text="5", padx=40, pady=20, command=lambda: button_click(5), bg="#93f0f5")
button_6 = Button(root, text="6", padx=40, pady=20, command=lambda: button_click(6), bg="#93f0f5")
button_7 = Button(root, text="7", padx=40, pady=20, command=lambda: button_click(7), bg="#93f0f5")
button_8 = Button(root, text="8", padx=40, pady=20, command=lambda: button_click(8), bg="#93f0f5")
button_9 = Button(root, text="9", padx=40, pady=20, command=lambda: button_click(9), bg="#93f0f5")
button_0 = Button(root, text="0", padx=40, pady=20, command=lambda: button_click(0), bg="#93f0f5")

button_add = Button(root, text="+", padx=39, pady=20, command=lambda: save("plus"), bg="#f4b3ff")
button_subtract = Button(root, text="-", padx=41, pady=20, command=lambda: save("subtract"), bg="#f4b3ff")
button_multiply = Button(root, text="x", padx=39, pady=20, command=lambda: save("multiply"), bg="#f4b3ff")
button_divide = Button(root, text="/", padx=43, pady=20, command=lambda: save("divide"), bg="#f4b3ff")

button_equal = Button(root, text="=", padx=150, pady=20, command=equals, bg="#eaf76f")
button_clear = Button(root, text="Clear", padx=17, pady=20, command=clear_entry, bg="#fab1bf")


# define font
myFont = font.Font(size=18)

all_buttons = [button_0, button_1, button_2, button_3, button_4, button_5, button_6, button_7, button_8, button_9, button_equal, button_clear, button_add, button_subtract, button_multiply, button_divide]
for button in all_buttons:
	button['font'] = myFont


# put buttons on screen
button_1.grid(row=3, column=0)
button_2.grid(row=3, column=1)
button_3.grid(row=3, column=2)

button_4.grid(row=2, column=0)
button_5.grid(row=2, column=1)
button_6.grid(row=2, column=2)

button_7.grid(row=1, column=0)
button_8.grid(row=1, column=1)
button_9.grid(row=1, column=2)

button_0.grid(row=4, column=0)

button_add.grid(row=4, column=1)
button_subtract.grid(row=4, column=2)
button_multiply.grid(row=5, column=0)
button_divide.grid(row=5, column=1)

button_clear.grid(row=5, column=2)
button_equal.grid(row=6, column=0, columnspan=3)


root.mainloop()
















