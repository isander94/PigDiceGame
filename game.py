import dice
import player
import cmd
import random

class Game():
    
    def __init__(self, player1, player2):
        self.player1 = player1
        self.player2 = player2
        
    def start(self):
        print("The game has started!")

        # Main loop
        while self.player1.get_score() < 20 or self.player2.get_score() < 20:
            
            keep_going = True
            round_score = 0

            while keep_going:
                roll = self.player1.roll_dice()
                print(f"{self.player1.get_name()} rolled a {roll}!")
                # If a player rolls 1, the score for this round is lost
                if(roll == 1):
                    round_score = 0
                    print(f"{self.player1.get_name()} loses all the points for this run!")
                    keep_going = False
                    break
                # Otherwise, the score is added to its total
                else:
                    round_score += roll
                    print(f"{self.player1.get_name()} now has {round_score} points!")
                # Ask the player to hold or roll again
                choice = input("Roll or Hold?")
                if choice.lower() == "roll":
                    keep_going = True
                elif choice.lower() == "hold":
                    self.player1.add_score(round_score)
                    keep_going = False
                    


    

    