from tkinter import *
from gameboard import tile_map
from random import randint

class Character():
    def __init__(self, x, y, canvas):
        self.canvas = canvas
        self.random_roll_dice = self.roll_dice()
        self.tile_size = 72
        self.x = x
        self.y = y

    def create_char(self, image):
        self.canvas.create_image(5 + self.x * self.tile_size, 5 + self.y * self.tile_size, image=image, anchor = NW)

    def roll_dice(self):
        random_roll_dice = randint(1, 6)
        return random_roll_dice

class Hero(Character):
    def __init__(self, canvas, x, y, tile_map):
        super().__init__(canvas,x, y)
        self.hero_image = PhotoImage(file = 'images/hero-down.gif')
        self.tile_map = tile_map
        self.max_health = 100
        self.current_health = max_health
        self.level = 1
        self.hp = 20 + (self.random_roll_dice * self.random_roll_dice * self.random_roll_dice)
        # self.current_hp =
        self.dp = self.random_roll_dice * self.random_roll_dice
        self.sp = 5 + (self.random_roll_dice)

    def draw_char(self):
        self.create_char(self.hero_image)

    def move_down(self, event):
        if self.tile_map[self.y+1][self.x] == 0:
            self.hero_image = PhotoImage(file = 'images/hero-down.gif')
            if self.y < 9:
                self.y += 1
            self.draw_char()

    def move_up(self, event):
        if self.tile_map[self.y-1][self.x] == 0:
            self.hero_image = PhotoImage(file = 'images/hero-up.gif')
            if self.y > 0:
                self.y = self.y - 1
            self.draw_char()

    def move_right(self, event):
        if self.tile_map[self.y][self.x+1] == 0:
            self.hero_image = PhotoImage(file = 'images/hero-right.gif')
            if self.x < 9:
                self.x = self.x + 1
            self.draw_char()

    def move_left(self, event):
        if self.tile_map[self.y][self.x-1] == 0:
            self.hero_image = PhotoImage(file = 'images/hero-left.gif')
            if self.x > 0:
                self.x = self.x - 1
            self.draw_char()

    # def attack(self):

class Boss(Character):

    def __init__(self, canvas, x, y):
        super().__init__(canvas,x, y)
        self.boss_image = PhotoImage(file = 'images/boss.gif')
        self.max_health = 100
        self.current_health = max_health
        self.level = 1
        self.hp = 2 * ((self.level * self.random_roll_dice) + self.random_roll_dice)
        # self.current_hp =
        self.dp = self.level/2 * (self.random_roll_dice + (self.random_roll_dice/2))
        self.sp = self.level * (self.random_roll_dice + self.level)

    def draw_char(self):
        self.create_char(self.boss_image)

class Skeleton(Character):
    def __init__(self, canvas, x, y):
        super().__init__(canvas,x, y)
        self.skeleton_image = PhotoImage(file = 'images/skeleton.gif')
        self.max_health = 100
        self.current_health = max_health
        self.level = 1
        self.hp = 2 * self.level * self.random_roll_dice
        # self.current_hp =
        self.dp = self.level/2 * self.random_roll_dice
        self.sp = self.level * self.random_roll_dice

    def draw_char(self):
        self.create_char(self.skeleton_image)
