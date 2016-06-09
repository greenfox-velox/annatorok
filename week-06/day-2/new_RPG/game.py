from char import *
from game_map import *
from tile import *

class Game():

    def __init__(self, canvas):
        self.canvas = canvas
        self.hero = Hero(0, 1)
        self.game_map = Map()
        # self.boss = Boss(0, 5, canvas)
        # self.skeleton = Skeleton(6, 8, canvas)
        # self.skeleton2 = Skeleton(0, 7, canvas)
        # self.skeleton3 = Skeleton(4, 5, canvas)
        # self.stat = Stat(canvas, hero)

    #
    #
    # def keyPressed(self, event):
    #     if event.keysym == 'Down':
    #         self.hero.move_down()
    #     if event.keysym == 'Right':
    #         self.hero.move_right()
    #     if event.keysym == 'Left':
    #         self.hero.move_left()
    #     if event.keysym == 'Up':
    #         self.hero.move_up()


    def draw_all(self):
        self.game_map.draw_tile(self.canvas)
        self.hero.draw_char(self.canvas)
        # self.boss.draw_char()
        # self.skeleton.draw_char()
        # self.skeleton2.draw_char()
        # self.skeleton3.draw_char()
        # self.stat.draw_text()
