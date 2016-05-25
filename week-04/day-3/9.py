from tkinter import *

# create a 300x300 canvas.
# create a square drawing function that takes 1 parameter:
# the square size
# and draws a square of that size to the center of the canvas.
# draw 3 squares with that function.


canvas_width = 300
canvas_height = 300

master = Tk()

canvas = Canvas(master, width=canvas_width, height=canvas_height)
canvas.pack()


def draw_square(square_size):

    x = canvas_width/2 - square_size/2
    y = canvas_height/2 - square_size/2
    square = canvas.create_rectangle(x, y, x+square_size, y+square_size,)

draw_square(100)
draw_square(70)
draw_square(25)

master.mainloop()
