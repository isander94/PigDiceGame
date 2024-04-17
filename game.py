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
        keep_going = True
        while self.player1.get_score() < 20 or self.player2.get_score() < 20:
            
            round_score = 0
            print("NEW ROUND")
            # Player 1 turn
            print(f"\n--- {self.player1.get_name()}'s turn ---")
            while keep_going:
                
                
                # Ask the player to roll or hold
                choice = input("Roll or Hold?\n--> ")

                if choice.lower() == "roll":
                    roll = self.player1.roll_dice()
                    if roll == 1:
                        print(f"{self.player1.get_name()} rolled a {roll} and loses all points for this turn!")
                        round_score = 0
                        break
                    else:
                        round_score += roll
                        print(f"{self.player1.get_name()} rolled a {roll} and now has {round_score} points!")

                elif choice.lower() == "hold":
                    self.player1.add_score(round_score)
                    print(f"{self.player1.get_name()} has secured {self.player1.get_score()} points!")
                    round_score = 0
                    break

            print(f"\n--- {self.player2.get_name()}'s turn ---")
            while keep_going:
                # Player 2's turn
                
                # Ask the player to roll or hold
                choice = input("Roll or Hold?\n--> ")

                if choice.lower() == "roll":
                    roll = self.player2.roll_dice()
                    if roll == 1:
                        print(f"{self.player2.get_name()} rolled a {roll} and loses all points for this turn!")
                        round_score = 0
                        break
                    else:
                        round_score += roll
                        print(f"{self.player2.get_name()} rolled a {roll} and now has {round_score} points!")

                elif choice.lower() == "hold":
                    self.player2.add_score(round_score)
                    print(f"{self.player2.get_name()} has secured {self.player2.get_score()} points!")
                    round_score = 0
                    break
                    

                
                    


    

    