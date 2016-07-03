from tile import Tile, Floor, Wall

tile_map = ([0, 0, 0, 1, 0, 1, 0, 0, 0, 0],
            [0, 0, 0, 1, 0, 1, 0, 1, 1, 0],
            [0, 1, 1, 1, 0, 1, 0, 1, 1, 0],
            [0, 0, 0, 0, 0, 1, 0, 0, 0, 0],
            [1, 1, 1, 1, 0, 1, 1, 1, 1, 0],
            [0, 1, 0, 1, 0, 0, 0, 0, 1, 0],
            [0, 1, 0, 1, 0, 1, 1, 0, 1, 0],
            [0, 0, 0, 0, 0, 1, 1, 0, 1, 0],
            [0, 1, 1, 1, 0, 0, 0, 0, 1, 0],
            [0, 0, 0, 1, 0, 1, 1, 0, 1, 0],
            [0, 1, 0, 1, 0, 1, 0, 0, 0, 0])

rows = 10
columns = 10

class Map():

    def __init__(self):
        self.map = []
        self.tile_map = tile_map

    def create_matrix_element(self, rows, columns):
        for x in range(rows):
            for y in range(columns):
                self.create_matrix_for_map(x, y)

    def create_matrix_for_map(self, x, y):
        if self.tile_map[y][x] == 0:
            self.map.append(Floor(x, y))
        else:
            self.map.append(Wall(x, y))

    def draw_tile(self, canvas):
        self.create_matrix_element(rows, columns)
        for tile in self.map:
            tile.draw(canvas)

    def check_edge(self, x, y):
        return y <= 9 and y >= 0 and x >= 0 and x <= 9

    def check_tile(self, x, y):
        return self.tile_map[y][x] == 0

    def is_this_tile_occupied(self, hero_x, hero_y, monster_position):
        if self.get_enemy(hero_x, hero_y, monster_position) == False:
            return False
        else:
            return True

    def can_move(self, hero_x, hero_y, x, y, monster_position):
        # print(self.is_this_tile_occupied(hero_x, hero_y, monster_position))
        # print(self.check_edge(x, y))
        # print(self.check_tile(x, y))
        return self.is_this_tile_occupied(hero_x, hero_y, monster_position) == False and self.check_edge(x, y) and self.check_tile(x, y)

    def get_enemy(self, hero_x, hero_y, monster_position):
        if hero_x == game.monster_position[0][0] and hero_y == game.monster_position[0][1]:
            return 'boss'
        elif hero_x == self.game.monster_position[1][0] and hero_y == self.game.monster_position[1][1]:
            return 'skeleton'
        elif hero_x == self.game.monster_position[2][0] and hero_y == self.game.monster_position[2][1]:
            return 'skeleton2'
        elif hero_x == self.game.monster_position[3][0] and hero_y == self.game.monster_position[3][1]:
            return 'skeleton3'
        else:
            return False
