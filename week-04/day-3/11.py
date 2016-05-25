from tkinter import *
import random

# create a 300x300 canvas.
# create a square drawing function that takes 2 parameters:
# the square size, and the fill color,
# and draws a square of that size and color to the center of the canvas.
# create a loop that fills the canvas with rainbow colored squares.


canvas_width = 300
canvas_height = 300

master = Tk()

canvas = Canvas(master, width=canvas_width, height=canvas_height)
canvas.pack()


def draw_square(square_size, color):
    x = canvas_width/2 - square_size/2
    y = canvas_height/2 - square_size/2
    square = canvas.create_rectangle(x, y, x+square_size, y+square_size, fill=color, outline='black')

for i in range(21, 0, -1):
    color = "#"+("%06x"%random.randint(0,16777215))
    draw_square(i*20, color)

master.mainloop()
