from tkinter import *

canvas_width = 300
canvas_height = 300

master = Tk()

canvas = Canvas(master, width=canvas_width, height=canvas_height)
canvas.pack()


def draw_square(square_size):
    x = 10
    for i in range(1, 7):
        square = canvas.create_rectangle(x, x, x + square_size, x + square_size, fill='purple')
        x = x + square_size
        square_size += 10


draw_square(10)

master.mainloop()
