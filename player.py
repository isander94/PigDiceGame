
from dice import Dice

class Player:
    def __init__(self, name, score):
        """Creates player class, user needs to input their name"""
        self.name = name
        self.score = score

    def change_name(self, new_name):
        """Allows the user to change their name"""
        self.name = new_name

    def get_name(self):
        """Gets the name of the player"""
        return self.name
    
    def get_score(self):
        """Gets the score of the player"""
        return self.score
    
    def add_score(self,score):
        """Adds to the score of the player"""
        self.score += score

        
