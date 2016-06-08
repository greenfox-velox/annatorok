from tile import *
from gameboard import *
from char import *

class Play():

    def __init__(self):
        master = Tk()
        canvas = Canvas(master, width = 1000, height = 720)

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

        skeleton = Skeleton(6, 8, canvas)
        skeleton.draw_char()

        skeleton2 = Skeleton(0, 7, canvas)
        skeleton2.draw_char()

        skeleton3 = Skeleton(4, 5, canvas)
        skeleton3.draw_char()

        canvas.pack()
        master.mainloop()

Play()
