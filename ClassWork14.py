# #GUI - Graphic User Interface
#
# #creating a graph:
# import matplotlib.pyplot as plt
# import numpy as np
# #import pandas as pd
#
# x = np.array(["c1", "c2", "c3", "c4"])
# y = np.array([80, 100, 62, 76])
#
# print(np.mean(y))
# print(np.median(y))
# print(np.std(y))
#
# plt.xlabel("Courses")
# plt.ylabel("Grades")
#
# plt.plot(x, y)
# plt.show()
#
# mylabels = ["a1", "a2", "a3", "a4"]
# plt.pie(y, labels=mylabels)
# plt.show()
#
# x1 = [2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019, 2020]
# y1 = [21, 19, 24, 17, 16, 25, 24, 22, 21, 21]
#
# plt.xlabel("Year")
# plt.ylabel("Number")
#
# plt.scatter(x1, y1)
# plt.show()

import tkinter
#pip install __

root = tkinter.Tk()
root.resizable(False, False)

myCanvas = tkinter.Canvas(root, bg="white", height = 600, width = 800)

#(x1, y1, x2, y2)
shape1 = myCanvas.create_oval(20,20,100,100, fill ="blue")
shape2 = myCanvas.create_oval(580,580,500,500, fill = "maroon")

velocities = {shape1: [3,3], shape2: [-3, -3]}


def move_shape(shape):
    global velocities
    xx, yy = velocities[shape]
    #
    myCanvas.move(shape, xx, yy)

    (x1, y1, x2, y2) = myCanvas.coords(shape)

    if x1 <= 0 or x2 >=800:
        xx = -xx
    if y1 <= 0 or y2 >= 600:
        yy = -yy

    velocities[shape] = [xx, yy]
    myCanvas.after(30, lambda: move_shape(shape))

myCanvas.after(10, lambda: move_shape(shape1))
myCanvas.after(10, lambda: move_shape(shape2))
myCanvas.pack()
root.mainloop()




