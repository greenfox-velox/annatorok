from tkinter import *

# create a 300x300 canvas.
# create a square drawing function that takes 2 parameters:
# the x and y coordinates of the square's top left corner
# and draws a 50x50 square from that point.
# draw 3 squares with that function.


canvas_width = 300
canvas_height = 300

master = Tk()

canvas = Canvas(master, width=canvas_width, height=canvas_height)
canvas.pack()

def draw_square(x,y):
    square = canvas.create_rectangle(x,y, x+50, y+50)

draw_square(70, 60)
draw_square(200, 90)
draw_square(150, 150)

master.mainloop()
