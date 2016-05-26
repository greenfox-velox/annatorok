from tkinter import *

# create a 300x300 canvas.
# draw a green 10x10 square to its center.


canvas_width = 300
canvas_height = 300

master = Tk()

square_size = 10
canvas = Canvas(master, width=canvas_width, height=canvas_height)
canvas.pack()

rectangle = canvas.create_rectangle(canvas_width/2 - square_size/2,  canvas_height/2 - square_size/2, canvas_width/2 + square_size/2,  canvas_height/2 + square_size/2)

master.mainloop()
