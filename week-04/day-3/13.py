# create a 300x300 canvas.
# create a line drawing function that takes 2 parameters:
# the x and y coordinates of the line's starting point
# and draws a line from that point to the center of the canvas.
# fill the canvas with lines from the edges, every 20 px, to the center.

from tkinter import *

master = Tk()

canvas_width = 300
canvas_height = 300

canvas = Canvas(master, width = canvas_width, height = canvas_height)
canvas.pack()


def create_line(x, y):
    line = canvas.create_line(x, y, canvas_width/2, canvas_height/2, fill='green')

for i in range(16):
    x = i * 20
    y = i * 20
    create_line(x, 0)
    create_line(x, 300)
    create_line(0, y)
    create_line(300, y)

master.mainloop()
