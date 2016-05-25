from tkinter import *

# create a 300x300 canvas.
# fill it with four different size and color rectangles.


canvas_width = 300
canvas_height = 300

master = Tk()

canvas = Canvas(master, width=canvas_width, height=canvas_height)
canvas.pack()

rectangle1 = canvas.create_rectangle(50, 50, 40, 40, fill='red')
rectangle2 = canvas.create_rectangle(200, 200, 300, 250, fill='green')
rectangle3 = canvas.create_rectangle(75, 75, 150, 90, fill='blue')
rectangle4 = canvas.create_rectangle(140, 140, 160, 300, fill='yellow')


master.mainloop()
