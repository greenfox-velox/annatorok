# create a pirate class
# it should have 2 methods
# drink_rum()
# hows_goin_mate()
# if the drink_rum was called at least 5 times:
# hows_goin_mate should return "Arrrr!"
# "Nothin'" otherwise

class Pirate:

    def __init__(self):
        self.x = 0

    def drink_rum(self):
        self.x += 1

    def hows_goin_mate(self):
        if self.x >= 5:
            return "Arrrr!"
        else:
            return "Nothin"


pirateA = Pirate()
pirateA.drink_rum()
pirateA.drink_rum()
pirateA.drink_rum()
print(pirateA.hows_goin_mate())
pirateA.drink_rum()
pirateA.drink_rum()
print(pirateA.hows_goin_mate())
