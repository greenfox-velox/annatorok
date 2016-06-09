from tkinter import *
from game_map import tile_map
from random import randint

class Character():
    def __init__(self, x, y):
        self.d6 = randint(1, 6)
        self.tile_size = 72
        self.x = x
        self.y = y

    def create_char(self, image, canvas):
        canvas.create_image(5 + self.x * self.tile_size, 5 + self.y * self.tile_size, image=image, anchor = NW)

class Hero(Character):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.hero_image = PhotoImage(file = 'images/hero-down.gif')
        # self.max_hp = 100
        # self.current_hp = 100
        # self.level = 1
        # self.name = 'Hero'
        # self.hp = 20 + self.d6 * self.d6 * self.d6
        # self.dp = self.d6 * self.d6
        # self.sp = 5 + self.d6

    def draw_char(self, canvas):
        self.create_char(self.hero_image, canvas)

    # def move_down(self):
    #     if self.hero.check_edge(self.y+1, self.x):
    #         self.hero_image = PhotoImage(file = 'images/hero-down.gif')
    #         if self.hero.check_floor(self.y+1, self.x):
    #             self.y += 1
    #     self.draw_char()
    #
    # def move_up(self):
    #     if self.check_edge(self.y-1, self.x):
    #         self.hero_image = PhotoImage(file = 'images/hero-up.gif')
    #         if self.check_floor(self.y-1, self.x):
    #             self.y -= 1
    #     self.draw_char()
    #
    # def move_right(self):
    #     if self.check_edge(self.y, self.x+1):
    #         self.hero_image = PhotoImage(file = 'images/hero-right.gif')
    #         if self.check_floor(self.y, self.x+1):
    #             self.x += 1
    #     self.draw_char()
    #
    # def move_left(self):
    #     if self.check_edge(self.y, self.x-1):
    #         self.hero_image = PhotoImage(file = 'images/hero-left.gif')
    #         if self.check_floor(self.y, self.x-1):
    #             self.x -= 1
    #     self.draw_char()


    # def attack(self):

    # def level_up(self):
	# 	self.max_hp += self.d6()
	# 	self.dp += self.d6()
	# 	self.sp += self.d6()

class Boss(Character):

    def __init__(self, x, y):
        super().__init__(x, y)
        self.boss_image = PhotoImage(file = 'images/boss.gif')
        # self.max_hp = 100
        # self.current_hp = 100
        # self.level = 1
        # self.name = 'Boss'
        # self.hp = 2 * ((self.level * self.d6) + self.d6)
        # self.dp = self.level/2 * (self.d6 + (self.d6/2))
        # self.sp = self.level * (self.d6 + self.level)

    def draw_char(self):
        self.create_char(self.boss_image)

class Skeleton(Character):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.skeleton_image = PhotoImage(file = 'images/skeleton.gif')
        # self.max_hp = 100
        # self.current_hp = 100
        # self.level = 1
        # self.name = 'Skeleton'
        # self.hp = 2 * self.level * self.d6
        # self.dp = self.level/2 * self.d6
        # self.sp = self.level * self.d6
#
    def draw_char(self):
        self.create_char(self.skeleton_image)
