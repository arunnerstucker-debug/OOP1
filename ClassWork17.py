import tkinter as tk
from tkinter import *

class Queue:
    def __init__(self):
        self.element = []
    def enqueue(self):
        x = valueTxt.get(1.0, "end-1c")
        self.element.append(x)
        valueTxt.delete(1.0, END)
    def dequeue(self):
        self.element.pop(0)
    def displayQueue(self):
        print("Elements in Queue:")
        valueTxt.delete(1.0, END)
        for i in self.element:
            valueTxt.insert(tk.INSERT, i)
            valueTxt.insert(tk.INSERT, ", ")
            print(i)
    def clearQueue(self):
        self.element.clear()

#main code
q = []
n = -1
def createQ():
    global n
    q.append(Queue())
    n += 1

top = Tk()
top.geometry("500x600")

valueTxt = Text(top, width=35, height=2)
valueTxt.place(x=100,y=100)

bcreateQ = Button(top, text = 'Create Q', width = 10, height =5, command=lambda: createQ())
bcreateQ.place(x=10, y = 150)

benqueue = Button(top, text = 'Enqueue', width = 10, height =5, command=lambda: q[n].enqueue())
benqueue.place(x=10, y = 250)

bdequeue = Button(top, text = 'Dequeue', width = 10, height =5, command=lambda: q[n].dequeue())
bdequeue.place(x=10, y = 350)

bdisplayqueue = Button(top, text = 'DisplayQueue', width = 10, height =5, command=lambda: q[n].displayQueue())
bdisplayqueue.place(x=10, y = 450)

bclearqueue = Button(top, text = "Clear Queue", width = 10, height= 5, command= lambda: q[n].clearQueue())
bclearqueue.place(x=110, y = 300)

valueTxt.delete(1.0, END)


top.mainloop()