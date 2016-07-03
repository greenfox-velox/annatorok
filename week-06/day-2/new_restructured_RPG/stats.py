from tkinter import *

class Stat():

    def __init__(self, hero, boss):
        self.hero = hero
        self.boss = boss
        self.x = 860
        self.y = 100

    def draw_hero_text(self, canvas):
        self.stat = self.hero.name + '\n' + '(Level ' + str(self.hero.level) + ')\nHP: ' + str(self.hero.hp) + '/' + str(self.hero.max_hp) + ' | DP: ' + str(self.hero.dp) + ' | SP: ' + str(self.hero.sp)
        canvas.create_text(self.x, self.y, text = self.stat)

    def draw_boss_text(self, canvas):
        self.stat = self.boss.name + '\n' + '(Level ' + str(self.boss.level) + ')\nHP: ' + str(self.boss.hp) + '/' + str(self.boss.max_hp) + ' | DP: ' + str(self.boss.dp) + ' | SP: ' + str(self.boss.sp)
        canvas.create_text(self.x, self.y + 200, text = self.stat)
