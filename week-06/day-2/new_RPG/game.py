from char import *
from game_map import *
from tile import *

class Game():

    def __init__(self, canvas):
        self.canvas = canvas
        self.hero = Hero(0, 1)
        self.game_map = Map()
        self.boss = Boss(0, 5)
        self.skeleton = Skeleton(6, 8)
        self.skeleton2 = Skeleton(0, 7)
        self.skeleton3 = Skeleton(4, 5)
        # self.stat = Stat(canvas, hero)

    #
    #
    def keyPressed(self, event):
        if event.keysym == 'Down':
            if self.game_map.check_edge(self.hero.x, self.hero.y+1) and self.game_map.check_floor(self.hero.x, self.hero.y+1):
                self.hero.move_down()
                self.hero.draw_char(self.canvas)
        if event.keysym == 'Right':
            if self.game_map.check_edge(self.hero.x+1, self.hero.y) and self.game_map.check_floor(self.hero.x+1, self.hero.y):
                self.hero.move_right()
                self.hero.draw_char(self.canvas)
        if event.keysym == 'Left':
            if self.game_map.check_edge(self.hero.x-1, self.hero.y) and self.game_map.check_floor(self.hero.x-1, self.hero.y):
                self.hero.move_left()
                self.hero.draw_char(self.canvas)
        if event.keysym == 'Up':
            if self.game_map.check_edge(self.hero.x, self.hero.y-1) and self.game_map.check_floor(self.hero.x, self.hero.y-1):
                self.hero.move_up()
                self.hero.draw_char(self.canvas)


    def draw_all(self):
        self.game_map.draw_tile(self.canvas)
        self.hero.draw_char(self.canvas)
        self.boss.draw_char(self.canvas)
        self.skeleton.draw_char(self.canvas)
        self.skeleton2.draw_char(self.canvas)
        self.skeleton3.draw_char(self.canvas)
        # self.stat.draw_text()
