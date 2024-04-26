
from dice import Dice
import random

class Computer:
    def __init__(self, diceLow, diceHigh):
        """Initializing the computer with different difficulty depending on dice"""
        self.score = 0
        self.dice = Dice(diceLow, diceHigh)

    def get_score(self):
        """Gets the computers score"""
        return self.score
    
    def add_score(self, score):
        """adds on to the computers score"""
        self.score += score

    def stay_or_roll(self):
        """The computer moves"""
        roll = self.dice.roll_dice()
        if roll == 1:
            return 0
        else:
            print(f"Computer rolled a {roll}")
            self.score += roll

        if self.get_score() < 10 or random.randint(0,1) == 1:
            print("Computer wants to roll again")
            roll = self.dice.roll_dice()
        else:
            self.add_score(self.score)
            print(f"computer stays with {self.get_score}")
            return 0
