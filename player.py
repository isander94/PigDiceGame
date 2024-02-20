
import dice

class Player:
    def __init__(self, name):
        """Creates player class, user needs to input their name"""
        self.name = name

    def change_name(self, new_name):
        """Allows the user to change their name"""
        self.name = new_name

