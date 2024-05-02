
"""Class representing a die that the player and computer can roll"""
import random


class Dice:
    """Creates a dice class with lowest and highest number"""
    def __init__(self, low, high):
        self.low = low
        self.high = high

    def roll_dice(self):
        """Rolls the dice for a number between lowest and highest given num"""
        random_num = random.randint(self.low, self.high)
        return random_num
