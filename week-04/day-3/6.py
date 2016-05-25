from tkinter import *

# create a 300x300 canvas.
# draw a green 10x10 square to its center.


canvas_width = 300
canvas_height = 300

master = Tk()

canvas = Canvas(master, width=canvas_width, height=canvas_height)
canvas.pack()

rectangle = canvas.create_rectangle(145, 145, 155, 155)

master.mainloop()
