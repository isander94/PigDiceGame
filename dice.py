import random
"""Class representing a die that the player and computer can roll"""


class Dice:
    def __init__(self, low, high):
        """Creates a dice class with lowest and highest number"""
        self.low = low
        self.high = high

    def roll_dice(self):
        """Rolls the dice for a number between lowest and highest given num"""
        random_num = random.randint(self.low, self.high)
        return random_num
