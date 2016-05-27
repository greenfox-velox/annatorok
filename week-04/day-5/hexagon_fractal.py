from tkinter import *

master = Tk()

canvas_size = 420

canvas = Canvas(master, width = canvas_size, height = canvas_size, bg='darkblue')
canvas.pack()


def hexa(x, y, size):
    triangle_height = (((3**0.5)/2)*size)
    canvas.create_polygon(x, y + triangle_height, x+size/2, y, x+size+size/2, y, x+size*2, y + triangle_height, x+size+size/2, y + triangle_height*2, x+size/2, y + triangle_height*2, fill='yellow', outline ='black')

    if size < 2: # base case
        pass
    else:
        triangle_height = (((3**0.5)/2)*size)
        s = size // 3
        hexa(x+size/3, y, s) #top left
        hexa(x+size, y, s) # top right
        hexa(x+size/3, y + triangle_height + triangle_height/3, s) # bottom left
        hexa(x+size, y + triangle_height + triangle_height/3, s) # bottom right
        hexa(x, y+2*triangle_height/3, s) # middle left
        hexa(x+size+size/3, y+2*triangle_height/3, s) # middle right

hexa(10, 10, 200)

master.mainloop()
