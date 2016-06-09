from tkinter import *

class Stat():

    def __init__(self, hero):
        self.hero = hero
        self.x = 760
        self.y = 100

    def draw_text(self, canvas):
        self.stat = self.hero.name + '(Level ' + str(self.hero.level) + ') HP: ' + str(self.hero.hp) + '/' + str(self.hero.max_hp) + ' | DP: ' + str(self.hero.dp) + ' | SP: ' + str(self.hero.sp)
        canvas.create_text(self.x, self.y, text = self.stat)
