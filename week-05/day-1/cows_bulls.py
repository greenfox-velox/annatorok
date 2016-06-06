# Create a class what is capable of playing exactly one game of Cows and Bulls (CAB). The player have to guess a 4 digit number. For every digit that the player guessed correctly in the correct place, they have a “cow”. For every digit the player guessed correctly in the wrong place is a “bull.”
#
# The CAB object should have a random 4 digit number, which is the goal to guess.
# The CAB object should have a state where the game state is stored (playing, finished).
# The CAB object should have a counter where it counts the guesses.
# The CAB object should have a guess method, which returns a string of the guess result
# All methods, including constructor should be tested

import random

class Cows_and_Bulls:

    def __init__(self):
        self.cows = 0
		self.bulls = 0
        self.counter = 0
        self.state = 'playing'


    def correct_number(self):
        self.correct_number = random.randint(1000,9999)
        return correct_number

    def guess_number(self, guess):
        if len(guess) < 4 or len(guess) > 4:
            state = 'finished'
            return False
        else:
            self.guess = guess
            self.counter += 1

    def guess():
        return
