
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

    def player_roll_dice(self):
        """Player rolling the dice"""
        turn_score = 0
        while True:
            nr_roll = Dice.roll_dice()
            turn_score += nr_roll
            total_score = turn_score + self.score

            print(self.name + " rolled a " + nr_roll)

            if total_score >= 25:
                print(self.name + " wins!")
                return self.get_score()


            if nr_roll == 1:
                print("Unlucky! You got a one! say bye bye to your points this round.")
                turn_score = 0
                break

            if nr_roll > 1:
                print(self.name + " Score this turn: " + turn_score )
                print(self.name + " Total score: " + total_score )

                decide = input("Roll again? (y/n): \n")
                while decide.lower() != ("y" or "n"):
                    decide = input("Error: Invalid input. Please only enter "'y'" or "'n'": ")

                if decide.lower() == "y":
                    continue
                elif decide.lower() == "n":
                    print(self.name + " Score this turn: " + turn_score )
                    print(self.name + " Total score: " + total_score )
                    self.add_score(turn_score)
                    break

            



        
