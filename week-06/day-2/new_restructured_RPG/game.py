from char import Character, Hero, Boss, Skeleton
from game_map import Map
from tile import Tile, Floor, Wall
from stats import Stat

class Game():

    def __init__(self, canvas):
        self.canvas = canvas
        self.game_map = Map()
        self.hero = Hero(0, 1)
        self.boss = Boss(0, 5)
        self.skeleton = Skeleton(6, 8)
        self.skeleton2 = Skeleton(0, 7)
        self.skeleton3 = Skeleton(4, 5)
        self.stat = Stat(self.hero, self.boss)
        self.monster_position()

    def monster_position(self):
        self.monster_position = [(self.boss.x,self.boss.y),(self.skeleton.x,self.skeleton.y),(self.skeleton2.x,self.skeleton2.y),(self.skeleton3.x,self.skeleton3.y)]

    def keyPressed(self, event):
        if event.keysym == 'Down':
            if self.game_map.can_move(self.hero.x, self.hero.y+1, self.hero.x, self.hero.y, self.monster_position):
            # if self.game_map.check_edge(self.hero.x, self.hero.y+1) and self.game_map.check_tile(self.hero.x, self.hero.y+1):
                self.hero.move_down()
            else:
                self.hero.turn_down()
            self.hero.draw_char(self.canvas)
        if event.keysym == 'Right':
            if self.game_map.check_edge(self.hero.x+1, self.hero.y) and self.game_map.check_tile(self.hero.x+1, self.hero.y):
                self.hero.move_right()
            else:
                self.hero.turn_right()
            self.hero.draw_char(self.canvas)
        if event.keysym == 'Left':
            if self.game_map.check_edge(self.hero.x-1, self.hero.y) and self.game_map.check_tile(self.hero.x-1, self.hero.y):
                self.hero.move_left()
            else:
                self.hero.turn_left()
            self.hero.draw_char(self.canvas)
        if event.keysym == 'Up':
            if self.game_map.check_edge(self.hero.x, self.hero.y-1) and self.game_map.check_tile(self.hero.x, self.hero.y-1):
                self.hero.move_up()
            else:
                self.hero.turn_up()
            self.hero.draw_char(self.canvas)
        if event.keysym == 'Space':
            self.battle()
        #
        # def start_the_battle(self):
        #     if self.game_map.is_this_tile_occupied(self.hero.x, self.hero.y, self.monster_position):
        #         self.strike(self.game_map.get_the_enemy(self.hero.x, self.hero.y, self.monster_position))
        #
        # def strike(self,attacker):
        #     if attacker == 'self.boss':
        #         # self.stat.draw_skeleton_boss
        #         self.strike_1 = self.hero.sp + self.d6 + self.d6
        #         self.strike_2 = self.boss.sp + self.d6 + self.d6
        #         if self.strike_1 > self.boss.dp:
        #             self.boss.damage(self.strike_1)
        #         if self.strike_2 + self.d6 + self.d6 > self.hero.dp:
        #             self.hero.damage(self.strike_2)
        #
        #
        #     elif attacker == 'self.skeleton':
        #         # self.stat.draw_skeleton_stat_1()
        #         self.strike_1 = self.hero.sp + self.d6 + self.d6
        #         self.strike_2 = self.skeleton.sp + self.dice + self.d6
        #         if self.strike_1 > self.skeleton.dp:
        #             self.skeleton.damage(self.strike_1)
        #         if self.strike_2 + self.d6+self.d6 > self.hero.dp:
        #             self.hero.damage(self.strike_2)
        #
        #
        #     elif attacker == 'self.skeleton2':
        #         # self.stat.draw_skeleton_stat_2()
        #         self.strike_1 = self.hero.sp+self.d6 + self.d6
        #         self.strike_2 = self.skeleton2.sp + self.dice + self.dice
        #         if self.strike_1 > self.skeleton2.self.dp:
        #             self.skeleton2.damage(self.strike_1)
        #         if self.strike_2 + self.d6 + self.d6 > self.hero.dp:
        #             self.hero.damage(self.strike_2)
        #
        #     elif attacker == 'self.skeleton3':
        #         # self.stat.draw_skeleton_stat_3()
        #         self.strike_1 = self.hero.sp + self.d6 + self.d6
        #         self.strike_2 = self.skeleton_3.sp + self.dice + self.d6
        #         if self.strike_1 > self.skeleton3.dp:
        #             self.skeleton3.damage(self.strike_1)
        #         if self.strike_2 + self.d6 + self.d6 > self.hero.dp:
        #             self.hero.damage(self.strike_2)

    def draw_all(self):
        self.game_map.draw_tile(self.canvas)
        self.hero.draw_char(self.canvas)
        self.boss.draw_char(self.canvas)
        self.skeleton.draw_char(self.canvas)
        self.skeleton2.draw_char(self.canvas)
        self.skeleton3.draw_char(self.canvas)
        self.stat.draw_hero_text(self.canvas)
        self.stat.draw_boss_text(self.canvas)
