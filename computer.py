
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
        round_score = 0
        while True:
            if round_score < 10 or random.randint(0, 1) == 1:
                print("Computer wants to roll again")
                roll = self.dice.roll_dice()
                if roll == 1:
                    print("computer rolled a 1 and loses all their points this round")
                    round_score = 0
                    break
                else:
                    round_score += roll
                    print(f"Computer rolled a {roll} and now has {self.get_score() + round_score}")
                if self.get_score() + round_score >= 20:
                    self.add_score(round_score)
                    break
                    
            else:
                self.add_score(round_score)
                print(f"computer stays with {self.get_score()}")
                break
            

            
