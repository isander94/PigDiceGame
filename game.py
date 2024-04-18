import dice
import player
import cmd
import random
import computer

class Game():
    def __init__(self):
        self.playing = True

    def Player_Computer(self):
        print("Welcome to Player vs Computer\n")
        name = input("Please enter your name: ")
        player1 = player.Player(name)

        print(f"Welcome {player1.get_name()}! Choose difficulty for the computer\n")
        diff = int(input(f"(1) Normal\n(2) Hard\n(3) Extreme (you wont win)\n---> "))
        computer1 = computer.Computer(1, (6 * diff))

        while self.playing:
            print(f"\n--- {player1.get_name()}'s turn ---")
            self.player_move(player1)

            if player1.get_score() >= 20:
                print(f"{player1.get_name()} wins with a score of {player1.get_score()}!")
                print("Game ended!")
                break

            print(f"\n--- Computer's turn ---")
            computer1.stay_or_roll()

            if computer1.get_score() >= 20:
                print(f"The computer wins with a score of {computer1.get_score()}!")
                print("Game ended!")
                break

    def Player_v_Player(self):
        """Method for two players playing against eachother"""
        print("Welcome to Player vs Player!\n")

        name = input("Please enter Player 1 name: ")
        player1 = player.Player(name)

        name2 = input("Please enter Player 2 name: ")
        player2 = player.Player(name2)

        print(f"Welcome {player1.get_name()} and {player2.get_name()}")

        while self.playing:
            print(f"\n--- {player1.get_name()}'s turn ---")
            self.player_move(player1)

            if player1.get_score() >= 20:
                print(f"{player1.get_name()} wins with a score of {player1.get_score()}!")
                print("Game ended!")
                break

            print(f"\n--- {player2.get_name()}'s turn ---")
            self.player_move(player2)

            if player2.get_score() >= 20:
                print(f"{player2.get_name()} wins with a score of {player2.get_score()}!")
                print("Game ended!")
                break


    def player_move(self, player0):
        round_score = 0
        while self.playing:

            choice = input("Roll or Hold?\n--> ")

            if choice.lower() == "roll":
                roll = player0.roll_dice()
                if roll == 1:
                    print(f"{player0.get_name()} rolled a {roll} and loses all points for this turn!")
                    round_score = 0
                    break
                else:
                    round_score += roll
                    print(f"{player0.get_name()} rolled a {roll} and now has {player0.get_score() + round_score} points!")
                if player0.get_score() + round_score >= 20:
                    player0.add_score(round_score)
                    break

            elif choice.lower() == "hold":
                player0.add_score(round_score)
                print(f"{player0.get_name()} has secured {player0.get_score()} points!")
                round_score = 0
                break



    '''def start(self):
        print("The game has started!")

        # Main loop
        keep_going = True
        while(keep_going):

            round_score = 0
            # Player 1 turn
            print(f"\n--- {self.player1.get_name()}'s turn ---")
            while(keep_going):
                # Ask the player to roll or hold
                choice = input("Roll or Hold?\n--> ")

                if(choice.lower() == "roll"):
                    roll = self.player1.roll_dice()
                    if(roll == 1):
                        print(f"{self.player1.get_name()} rolled a {roll} and loses all points for this turn!")
                        round_score = 0
                        break
                    else:
                        round_score += roll
                        print(f"{self.player1.get_name()} rolled a {roll} and now has {self.player1.get_score() + round_score} points!")

                elif(choice.lower() == "hold"):
                    self.player1.add_score(round_score)
                    print(f"{self.player1.get_name()} has secured {self.player1.get_score()} points!")
                    round_score = 0
                    break
            
            # Check score
            if(self.player1.get_score() >= 20):
                print(f"{self.player1.get_name()} wins with a score of {self.player1.get_score()}!")
                print("Game ended!")
                break

            # Player 2's turn
            print(f"\n--- {self.player2.get_name()}'s turn ---")
            while(keep_going):
                # Ask the player to roll or hold
                choice = input("Roll or Hold?\n--> ")

                if(choice.lower() == "roll"):
                    roll = self.player2.roll_dice()
                    if(roll == 1):
                        print(f"{self.player2.get_name()} rolled a {roll} and loses all points for this turn!")
                        round_score = 0
                        break
                    else:
                        round_score += roll
                        print(f"{self.player2.get_name()} rolled a {roll} and now has {self.player2.get_score() + round_score} points!")

                elif(choice.lower() == "hold"):
                    self.player2.add_score(round_score)
                    print(f"{self.player2.get_name()} has secured {self.player2.get_score()} points!")
                    round_score = 0
                    break

                # Check score
            if(self.player2.get_score() >= 20):
                print(f"{self.player2.get_name()} wins with a score of {self.player2.get_score()}!")
                print("Game ended!")
                break'''
                    

                
                    


    

    