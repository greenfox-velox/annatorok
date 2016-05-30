# Create a class what is capable of playing exactly one game of Cows and Bulls (CAB). The player have to guess a 4 digit number. For every digit that the player guessed correctly in the correct place, they have a “cow”. For every digit the player guessed correctly in the wrong place is a “bull.”
#
# The CAB object should have a random 4 digit number, which is the goal to guess.
# The CAB object should have a state where the game state is stored (playing, finished).
# The CAB object should have a counter where it counts the guesses.
# The CAB object should have a guess method, which returns a string of the guess result
# All methods, including constructor should be tested


class Cab:

    def __init__(self, number):
        self.number = number
