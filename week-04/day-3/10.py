from tkinter import *


# create a 300x300 canvas.
# create a square drawing function that takes 1 parameter:
# the square size
# and draws a square of that size to the center of the canvas.
# create a loop that draws 20 squares with that function.


canvas_width = 300
canvas_height = 300

master = Tk()

canvas = Canvas(master, width=canvas_width, height=canvas_height)
canvas.pack()


def draw_square(square_size):
    x = canvas_width/2 - square_size/2
    y = canvas_height/2 - square_size/2
    square = canvas.create_rectangle(x, y, x+square_size, y+square_size, fill='green', outline='black')

for i in range(21, 0, -1):
    draw_square(i*20)


master.mainloop()
