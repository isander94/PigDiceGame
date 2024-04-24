from dice import Dice

"""Class representing a player controlled by the computer"""

class Cpu_player:
    def __init__(self, difficulty):
        self.difficulty = difficulty
        self.score
        self.dice = Dice()

    def cpu_roll_dice(self):
        self.dice.roll_dice()