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

class Stack:
    def __init__(self):
        self.element = []
    def push(self):
        self.element.append((valueTxt.get(1.0, "end-1c")))
        valueTxt.delete(1.0, END)
    def pop(self):
        self.element.pop()
    def displayStack(self):
        print("elements in stack: ")
        valueTxt.delete(1.0, END)
        for i in self.element:
            valueTxt.insert(tk.INSERT, i)
            valueTxt.insert(tk.INSERT, ", ")
            print(i)
    def clearStack(self):
        self.element.clear()


#main code
s = []
n = -1

q = []
i = -1

def createS():
    global s, n, i
    x = []
    x.append(i)
    s.append(Stack())
    n += 1

def createQ():
    global i, n, q
    x = []
    x.append(n)
    q.append(Queue())
    i += 1

top = Tk()
top.geometry("500x600")

valueTxt = Text(top, width=35, height=2)
valueTxt.place(x=100,y=100)

bcreateS = Button(top, text = "Create S", width = 10, height =5, command=lambda: createS())
bcreateS.place(x=10, y = 150)

bpush = Button(top, text = 'Push', width = 10, height =5, command=lambda: s[n].push())
bpush.place(x=10, y = 250)

bpop = Button(top, text = 'Pop', width = 10, height =5, command=lambda: s[n].pop())
bpop.place(x=10, y = 350)

bdisplayStack = Button(top, text = 'Display Stack', width = 10, height =5, command=lambda: s[n].displayStack())
bdisplayStack.place(x=10, y = 450)

bclearStack = Button(top, text = "Clear Stack", width = 10, height= 5, command= lambda: s[n].clearStack())
bclearStack.place(x=210, y = 300)

bcreateQ = Button(top, text = 'Create Q', width = 10, height =5, command=lambda: createQ())
bcreateQ.place(x=110, y = 150)

benqueue = Button(top, text = 'Enqueue', width = 10, height =5, command=lambda: q[i].enqueue())
benqueue.place(x=110, y = 250)

bdequeue = Button(top, text = 'Dequeue', width = 10, height =5, command=lambda: q[i].dequeue())
bdequeue.place(x=110, y = 350)

bdisplayqueue = Button(top, text = 'DisplayQueue', width = 10, height =5, command=lambda: q[i].displayQueue())
bdisplayqueue.place(x=110, y = 450)

bclearqueue = Button(top, text = "Clear Queue", width = 10, height= 5, command= lambda: q[i].clearQueue())
bclearqueue.place(x=210, y = 200)

valueTxt.delete(1.0, END)

top.mainloop()
