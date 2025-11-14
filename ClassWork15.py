#Calculator
import tkinter as tk
from tkinter import *

top = Tk()
top.geometry("500x600")

answer = Text(width=35, height=2)
answer.place(x=100,y=100)

i = 0
buttons = []
def show(x):
    global i
    buttons.append(x)
    try:
        if buttons[i] == "=":
            final_answer = eval(answer.get(1.0, "end-1c"))
            buttons.append(final_answer)
            answer.insert(tk.INSERT, buttons[i])
            i+= 1
            answer.insert(tk.INSERT, final_answer)
            i+=1
        elif buttons[i] == "Clear":
            answer.delete(1.0, END)
            buttons.clear()
            i = 0
        elif buttons[i] == "Back":

        else:
            answer.insert(tk.INSERT, buttons[i])
            i+=1
    except:
        answer.delete(1.0, END)
        answer.insert(tk.INSERT, buttons[i])


BClear = Button(top, text = 'Clear', width = 10, height =5, command= lambda: show("Clear"))
BClear.place(x=10, y = 150)

BBack = Button(top, text = 'Back', width = 10, height =5, command= lambda: show("Back"))
BBack.place(x=10, y = 250)

B0 = Button(top, text = '0', width = 10, height =5, command= lambda: show("0"))
B0.place(x=200, y = 475)

B1 = Button(top, text = '1', width = 10, height =5, command= lambda: show("1"))
B1.place(x=100, y=375)

B2 = Button(top, text = '2', width = 10, height =5, command= lambda: show("2"))
B2.place(x=200, y = 375)

B3 = Button(top, text = '3', width = 10, height =5, command= lambda: show("3"))
B3.place(x=300, y = 375)

B4 = Button(top, text = '4', width = 10, height =5, command= lambda: show("4"))
B4.place(x=100, y = 275)

B5 = Button(top, text = '5', width = 10, height =5, command= lambda: show("5"))
B5.place(x=200, y = 275)

B6 = Button(top, text = '6', width = 10, height =5, command= lambda: show("6"))
B6.place(x=300, y = 275)

B7 = Button(top, text = '7', width = 10, height =5, command= lambda: show("7"))
B7.place(x=100, y = 175)

B8 = Button(top, text = '8', width = 10, height =5, command= lambda: show("8"))
B8.place(x=200, y = 175)

B9 = Button(top, text = '9', width = 10, height =5, command= lambda: show("9"))
B9.place(x=300, y = 175)

B10 = Button(top, text = '+', width = 10, height =5, command= lambda: show("+"))
B10.place(x=400, y = 100)

B11 = Button(top, text = '-', width = 10, height =5, command= lambda: show("-"))
B11.place(x=400, y = 200)

B12 = Button(top, text = '*', width = 10, height =5, command= lambda: show("*"))
B12.place(x=400, y = 300)

B13 = Button(top, text = '/', width = 10, height =5, command= lambda: show("/"))
B13.place(x=400, y = 400)

B14 = Button(top, text = '=', width = 10, height =5, command= lambda: show("="))
B14.place(x=400, y = 500)

top.mainloop()
