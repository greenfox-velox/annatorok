from tkinter import *


# create a 300x300 canvas.
# draw a box that has different colored lines on each edge.


master = Tk()

canvas = Canvas(master, width='300', height='300')
canvas.pack()

redline = canvas.create_line(50, 100, 50, 200, fill='red')
greenline = canvas.create_line(50, 100, 150, 100, fill='green')
blueline = canvas.create_line(150, 100, 150, 200, fill='blue')
yellowline = canvas.create_line(150, 200, 50, 200, fill='yellow')


master.mainloop()
