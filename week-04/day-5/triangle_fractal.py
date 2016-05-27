from tkinter import *

master = Tk()

canvas_size = 600

canvas = Canvas(master, width = canvas_size, height = canvas_size)
canvas.pack()


def triangle(x, y, size):
    triangle_height = (((3**0.5)/2)*size)
    canvas.create_polygon(x, y, x + size, y, x+size/2, y + triangle_height, fill='green', outline ='black')

    if size < 2:
        pass
    else:
        triangle_height = (((3**0.5)/2)*size)
        s = size // 2
        triangle(x, y, s)
        triangle(x+size/2, y, s)
        triangle(x+size/4, y+triangle_height/2, s)

triangle(0, 0, 600)

master.mainloop()


# (0, 0, 600, 0, 300, 600)

# this is square fractal
# from tkinter import *
#
# master = Tk()
#
# canvas_size = 600
#
# canvas = Canvas(master, width = canvas_size, height = canvas_size, bg = 'yellow')
# canvas.pack()
#
# def fractal(x, y, size):
#     canvas.create_rectangle(x, y, x + size, y + size, fill="yellow")
#     if size < 5:
#         pass
#     else:
#         s = size // 3
#         fractal(x + size/3, y, s)
#         fractal(x, y + size/3, s)
#         fractal(x + 2*size/3, y + size/3, s)
#         fractal(x + size/3, y + 2*size/3, s)
#
# fractal(0, 0, 600)
#
# master.mainloop()
