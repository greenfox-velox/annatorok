from tkinter import *

# create a 300x300 canvas.
# create a line drawing function that takes 2 parameters:
# the x and y coordinates of the line's starting point
# and draws a line from that point to the center of the canvas.
# draw 3 lines with that function.
canvas_width = 300
canvas_height = 300

master = Tk()

canvas = Canvas(master, width=canvas_width, height=canvas_height)
canvas.pack()

def create_line(x, y):
        line1 = canvas.create_line(x, y, canvas_width/2, canvas_height/2)

create_line(0, 0)
create_line(0, 150)
create_line(150, 0)

master.mainloop()
