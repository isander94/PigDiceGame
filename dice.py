import random

class Dice:
    def __init__(self):
        self.low = 1
        self.high = 6

    def roll_dice(self):
        random_num = random.randint(self.low, self.high)
        return random_num
    
