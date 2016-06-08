from tile import *
from gameboard import *
from char import *

class Play():

    def __init__(self):
        master = Tk()
        canvas_size = 720
        canvas = Canvas(master, width = canvas_size, height = canvas_size)

        game = Gameboard(canvas)
        game.draw_gameboard()

        hero = Hero(0, 1, canvas, tile_map)
        hero.draw_char()

        master.bind('<Down>', hero.move_down)
        master.bind('<Up>', hero.move_up)
        master.bind('<Right>', hero.move_right)
        master.bind('<Left>', hero.move_left)

        boss = Boss(0, 5, canvas)
        boss.draw_char()

        skeleton = Skeleton(4, 5, canvas)
        skeleton.draw_char()

        canvas.pack()
        master.mainloop()

Play()
