from tkinter import *

class Stat():

    def __init__(self, canvas, hero):
        self.canvas = canvas
        self.hero = hero
        self.x = 760
        self.y = 100

    def draw_text(self):
        self.stat = self.hero.name + '(Level ' + str(self.hero.level) + ') HP: ' + str(self.hero.hp) + '/' + str(self.hero.max_hp) + ' | DP: ' + str(self.hero.dp) + ' | SP: ' + str(self.hero.sp)
        self.canvas.create_text(self.x, self.y, text = self.stat)
