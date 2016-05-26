# reproduce this: [https://github.com/greenfox-velox/velox-syllabus/blob/master/week-04/3-graphics/workshop/r1.png]
# divide the canvas into 4 parts and repeat the pattern.
# reproduce this: [https://github.com/greenfox-velox/velox-syllabus/blob/master/week-04/3-graphics/workshop/r2.png]
# can you make the colors change? make every line a different color.


from tkinter import *

master = Tk()

canvas_width = 300
canvas_height = 300

canvas = Canvas(master, width = canvas_width, height = canvas_height)
canvas.pack()

def create_line(x,y):
    greenline = canvas.create_line(0,0,150,150, fill='green')

for i in range(16):
    x = i * 20
    y = i * 20
    create_line(x, 0)

master.mainloop()
