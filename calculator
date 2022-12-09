# calculator

from tkinter import *

root = Tk()
root.title("Calculator")

e = Entry(root, width=55, borderwidth=5)
e.grid(row=0, column=0, columnspan=3)


def button_click(number):
    current = e.get()
    e.delete(0, END)
    e.insert(0, str(current) + str(number))


def clear():
    e.delete(0, END)


def button_add():
    first_number = e.get()
    global f_num
    global math
    math = "addition"
    f_num = float(first_number)
    e.delete(0, END)


def equal():
    second_number = e.get()
    e.delete(0, END)
    if math == "addition":
        e.insert(0, float(f_num) + float(second_number))
    if math == "subtract":
        e.insert(0, float(f_num) - float(second_number))
    if math == "multiply":
        e.insert(0, float(f_num) * float(second_number))
    if math == "divide":
        e.insert(0, float(f_num) / float(second_number))


def multiply():
    first_number = e.get()
    global f_num
    global math
    math = "multiply"
    f_num = float(first_number)
    e.delete(0, END)


def divide():
    first_number = e.get()
    global f_num
    global math
    math = "divide"
    f_num = float(first_number)
    e.delete(0, END)


def subtract():
    first_number = e.get()
    global f_num
    global math
    math = "subtract"
    f_num = float(first_number)
    e.delete(0, END)


button_1 = Button(root, text="1", pady=30, padx=50, command=lambda: button_click(1))
button_2 = Button(root, text="2", pady=30, padx=50, command=lambda: button_click(2))
button_3 = Button(root, text="3", pady=30, padx=50, command=lambda: button_click(3))
button_4 = Button(root, text="4", pady=30, padx=50, command=lambda: button_click(4))
button_5 = Button(root, text="5", pady=30, padx=50, command=lambda: button_click(5))
button_6 = Button(root, text="6", pady=30, padx=50, command=lambda: button_click(6))
button_7 = Button(root, text="7", pady=30, padx=50, command=lambda: button_click(7))
button_8 = Button(root, text="8", pady=30, padx=50, command=lambda: button_click(8))
button_9 = Button(root, text="9", pady=30, padx=50, command=lambda: button_click(9))
button_0 = Button(root, text="0", pady=30, padx=50, command=lambda: button_click(0))

button_equal = Button(root, text="=", pady=30, padx=105, command=equal)
button_clear = Button(root, text="clear", pady=30, padx=97, command=clear)

button_add = Button(root, text="+", pady=30, padx=49, command=button_add)
button_multiply = Button(root, text="*", pady=30, padx=50, command=multiply)
button_divide = Button(root, text="/", pady=30, padx=50, command=divide)
button_subtract = Button(root, text="-", pady=30, padx=50, command=subtract)

button_1.grid(row=1, column=0, )
button_2.grid(row=1, column=1, )
button_3.grid(row=1, column=2, )

button_4.grid(row=2, column=0, )
button_5.grid(row=2, column=1, )
button_6.grid(row=2, column=2, )

button_7.grid(row=3, column=0, )
button_8.grid(row=3, column=1, )
button_9.grid(row=3, column=2, )

button_add.grid(row=5, column=0)
button_multiply.grid(row=6, column=0, )
button_divide.grid(row=6, column=1, )
button_subtract.grid(row=6, column=2, )

button_equal.grid(row=5, column=1, columnspan=2)

button_0.grid(row=4, column=0, )
button_clear.grid(row=4, column=1, columnspan=2)
