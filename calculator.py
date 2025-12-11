import tkinter as tk
from tkinter import *
window = tk.Tk()
window.title("Calculator")
window.geometry("400x400")

e= tk.Entry(window, width=100, borderwidth=5)
e.place(x = 0, y = 0)
def button_clicked(number):
    current = e.get()
    e.delete(0, tk.END)
    e.insert(0, current + str(number))
b= Button(window, text="1", width=10, command=lambda:button_clicked(1))
b.place(x =10, y = 60)
b= Button(window, text="2", width=10, command=lambda:button_clicked(2))
b.place(x =80, y = 60)

b= Button(window, text="3", width=10, command=lambda:button_clicked(3))
b.place(x =160, y = 60)

b= Button(window, text="4", width=10, command=lambda:button_clicked(4))
b.place(x =10, y = 110)

b= Button(window, text="5", width=10, command=lambda:button_clicked(5))
b.place(x =80, y = 110)

b= Button(window, text="6", width=10, command=lambda:button_clicked(6))
b.place(x =160, y = 110)

b= Button(window, text="7", width=10, command=lambda:button_clicked(7))
b.place(x =10, y = 180)

b= Button(window, text="8", width=10, command=lambda:button_clicked(8))
b.place(x =80, y = 180)

b= Button(window, text="9", width=10, command=lambda:button_clicked(9))
b.place(x =160, y = 180)

b= Button(window, text="0", width=10, command=lambda:button_clicked(0))
b.place(x =10, y = 240)

def sum():
    global i
    global math
    math="addition"
    n1 = e.get()
    i = int(n1)
    e.delete(0, END)

b= Button(window, text="+", width=10, command=sum)
b.place(x =80, y = 240)
def sub():
    global i
    global math
    math="subtraction"
    n1= e.get()
    i=int(n1)
    e.delete(0,END)
b= Button(window, text="-", width=10, command=sub)
b.place(x =160, y = 240)
b.place(x =160, y = 240)
def div():
    global i
    global math
    math="division"
    n1 = e.get()
    i = int(n1)
    e.delete(0, END)


b= Button(window, text="/", width=10, command=div)
b.place(x =10, y = 300)
def mul():
    global i
    global math
    math="multiplication"
    n1 = e.get()
    i = int(n1)
    e.delete(0, END)


b= Button(window, text="*", width=10, command=mul)

b.place(x =80, y = 300)
def enter():
    n2=e.get()
    e.delete(0, END)
    if math=="addition":
        e.insert(0,i + int(n2))
    elif math=="subtraction":
        e.insert(0,i - int(n2))
    elif math=="multiplication":
        e.insert(0,i * int(n2))
    else:
        e.insert(0,i / int(n2))


b= Button(window, text="=", width=10, command=enter)
b.place(x =160, y = 300)
def clear():
    e.delete(0, END)
b= Button(window, text="Clear", width=10, command=clear)
b.place(x =10, y = 350)

window.mainloop()