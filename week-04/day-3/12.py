from tkinter import *

master = Tk()

canvas_width = 320
canvas_height = 320

canvas = Canvas(master, width = canvas_width, height = canvas_height, bg = 'white')
canvas.pack()

x = 0
y = 0
square_size = 40

for i in range(1,9):
    x = 0
    for j in range(1, 9):
        if (i+j) % 2 ==0:
            color = 'white'
        else:
            color = 'black'
        rect = canvas.create_rectangle(x, y, x + square_size, y + square_size, fill=color)
        x += square_size
    y += square_size


master.mainloop()
