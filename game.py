import player
import computer
import highscore


class Game():
    def __init__(self):
        self.playing = True
        self.highscore = highscore.Highscore()

    def Player_Computer(self):
        print("Welcome to Player vs Computer\n")
        name = input("Please enter your name: ")
        player1 = player.Player(name)

        print(f"Welcome {player1.get_name()}! Choose difficulty for the computer\n")

        input_error = True
        out_of_bounds = True
        while (input_error):
            try:
                # Check if the input is out of bounds - There are only three difficulty settings
                while (out_of_bounds):
                    diff = int(input(f"(1) Normal\n(2) Hard\n(3) Extreme (you wont win)\n---> "))
                    if (diff < 1 or diff > 3):
                        print("Invalid input - Try again!")
                        out_of_bounds = True
                    else:
                        out_of_bounds = False
            except (ValueError):
                print("Invalid input - Try again!")
            else:
                input_error = False

        computer1 = computer.Computer(1, (6 * diff))

        while self.playing:
            print(f"\n--- {player1.get_name()}'s turn ---")
            quit = self.player_move(player1)

            if player1.get_score() >= 20:
                print(f"{player1.get_name()} wins with a score of {player1.get_score()}!")
                print("Game ended!")
                self.highscore.add_highscore(player1.get_name(), player1.get_score())
                break
            elif quit == 0:
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
            quit = self.player_move(player1)

            if player1.get_score() >= 20:
                print(f"{player1.get_name()} wins with a score of {player1.get_score()}!")
                print("Game ended!")
                self.highscore.add_highscore(player1.get_name(), player1.get_score())
                break
            elif quit == 0:
                break

            print(f"\n--- {player2.get_name()}'s turn ---")
            quit = self.player_move(player2)

            if player2.get_score() >= 20:
                print(f"{player2.get_name()} wins with a score of {player2.get_score()}!")
                print("Game ended!")
                self.highscore.add_highscore(player2.get_name(), player2.get_score())
                break

            elif quit == 0:
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

            elif choice.lower() == "changename":
                new_name = input("Enter new name:\n--> ")
                player0.name = new_name

            elif choice.lower() == "quit":
                return 0
