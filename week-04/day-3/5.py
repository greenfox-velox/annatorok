from tkinter import *

# create a 300x300 canvas.
# create a line drawing function that takes 2 parameters:
# the x and y coordinates of the line's starting point
# and draws a 50 long horizontal line from that point.
# draw 3 lines with that function.


canvas_width = 300
canvas_height = 300

master = Tk()

canvas = Canvas(master, width=canvas_width, height=canvas_height)
canvas.pack()

def create_line(x, y):
        line = canvas.create_line(x, y, x+50, y)

create_line(50, 50)
create_line(50, 150)
create_line(150, 200)

master.mainloop()
