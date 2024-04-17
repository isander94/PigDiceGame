import random

"""Class representing a die that the player and computer controlled player can roll"""
class Dice:
    def __init__(self, low, high):
        """Creates a dice class with low number 1 and high number 6, representing a 6-faced die"""
        self.low = low
        self.high = high

    def roll_dice(self):
        """Rolls the dice for a number between 1 and 6"""
        random_num = random.randint(self.low, self.high)
        return random_num