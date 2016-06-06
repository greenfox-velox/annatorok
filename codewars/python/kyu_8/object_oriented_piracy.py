# Every time your spies see a new ship enter the dock, they will create a new ship object:
#
# Titanic = Ship(15,10)
# Now comes the tricky part: An average man will sink the ship by exactly 1.5 units. (Ship's draft goes up) That means the draft can show the estimated weight of the presumable booty aboard.
#
# if it weighs more than 20 without people, it is worthy to board. Your system should have a method
#
# is_worth_it
# to decide that:
#
# Titanic.is_worth_it() #return false

class Ship:
    def __init__(self, draft, crew):
        self.draft = draft
        self.crew = crew
    def is_worth_it(self):
        if (self.draft - self.crew*1.5 > 20):
            return True
        else:
            return False
