from tkinter import *
from gameboard import tile_map
from random import randint

class Character():
    def __init__(self, x, y, canvas):
        self.canvas = canvas
        self.random_roll_dice = self.roll_dice()
        # self.stat = self.stats()
        self.tile_size = 72
        self.x = x
        self.y = y

    def create_char(self, image):
        self.canvas.create_image(5 + self.x * self.tile_size, 5 + self.y * self.tile_size, image=image, anchor = NW)

    def roll_dice(self):
        random_roll_dice = randint(1, 6)
        return random_roll_dice

    # def stats(self):
    #     stat = self.name + '(Level ' + str(self.level) + ') HP: ' + str(self.hp) + '/' + str(self.max_hp) + ' | DP: ' + str(self.dp) + ' | SP: ' + str(self.sp)
    #     return stat

class Hero(Character):
    def __init__(self, canvas, x, y, tile_map):
        super().__init__(canvas,x, y)
        self.hero_image = PhotoImage(file = 'images/hero-down.gif')
        self.tile_map = tile_map
        self.max_hp = 100
        self.current_hp = 100
        self.level = 1
        # self.name = 'Hero'
        self.hp = 20 + (self.random_roll_dice * self.random_roll_dice * self.random_roll_dice)
        self.dp = self.random_roll_dice * self.random_roll_dice
        self.sp = 5 + self.random_roll_dice
        self.stat = 'Hero + (Level ' + str(self.level) + ') HP: ' + str(self.hp) + '/' + str(self.max_hp) + ' | DP: ' + str(self.dp) + ' | SP: ' + str(self.sp)


    def draw_char(self):
        self.create_char(self.hero_image)

    def move_down(self):
        if self.check_edge(self.y+1, self.x):
            self.hero_image = PhotoImage(file = 'images/hero-down.gif')
            if self.check_floor(self.y+1, self.x):
                self.y += 1
        self.draw_char()

    def move_up(self):
        if self.check_edge(self.y-1, self.x):
            self.hero_image = PhotoImage(file = 'images/hero-up.gif')
            if self.check_floor(self.y-1, self.x):
                self.y -= 1
        self.draw_char()

    def move_right(self):
        if self.check_edge(self.y, self.x+1):
            self.hero_image = PhotoImage(file = 'images/hero-right.gif')
            if self.check_floor(self.y, self.x+1):
                self.x += 1
        self.draw_char()

    def move_left(self):
        if self.check_edge(self.y, self.x-1):
            self.hero_image = PhotoImage(file = 'images/hero-left.gif')
            if self.check_floor(self.y, self.x-1):
                self.x -= 1
        self.draw_char()

    def check_edge(self, y, x):
        return y <= 9 and y >= 0 and x >= 0 and x <= 9

    def check_floor(self, y, x):
        return self.tile_map[y][x] == 0

    # def attack(self):

    # def level_up(self):
	# 	self.max_hp += self.d6()
	# 	self.dp += self.d6()
	# 	self.sp += self.d6()

class Boss(Character):

    def __init__(self, canvas, x, y):
        super().__init__(canvas,x, y)
        self.boss_image = PhotoImage(file = 'images/boss.gif')
        self.max_hp = 100
        self.current_hp = 100
        self.level = 1
        # self.name = 'Boss'
        self.hp = 2 * ((self.level * self.random_roll_dice) + self.random_roll_dice)
        self.dp = self.level/2 * (self.random_roll_dice + (self.random_roll_dice/2))
        self.sp = self.level * (self.random_roll_dice + self.level)
        self.stat = 'Boss + (Level ' + str(self.level) + ') HP: ' + str(self.hp) + '/' + str(self.max_hp) + ' | DP: ' + str(self.dp) + ' | SP: ' + str(self.sp)

    def draw_char(self):
        self.create_char(self.boss_image)

class Skeleton(Character):
    def __init__(self, canvas, x, y):
        super().__init__(canvas,x, y)
        self.skeleton_image = PhotoImage(file = 'images/skeleton.gif')
        self.max_hp = 100
        self.current_hp = 100
        self.level = 1
        # self.name = 'Skeleton'
        self.hp = 2 * self.level * self.random_roll_dice
        self.dp = self.level/2 * self.random_roll_dice
        self.sp = self.level * self.random_roll_dice
        self.stat = 'Skeleton + (Level ' + str(self.level) + ') HP: ' + str(self.hp) + '/' + str(self.max_hp) + ' | DP: ' + str(self.dp) + ' | SP: ' + str(self.sp)


    def draw_char(self):
        self.create_char(self.skeleton_image)
