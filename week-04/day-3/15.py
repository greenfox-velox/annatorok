# csillag

from tkinter import *

master = Tk()

canvas_size = 400

canvas = Canvas(master, width = canvas_size, height = canvas_size)
canvas.pack()

half = canvas_size // 2

for i in range(0, half+1, 20):
    canvas.create_line(i, half, half, half-i, fill='green')
    canvas.create_line(canvas_size-i, half, half, half-i, fill='green')
    canvas.create_line(i, half, half, half+i, fill='green')
    canvas.create_line(canvas_size-i, half, half, half+i, fill='green')

master.mainloop()
