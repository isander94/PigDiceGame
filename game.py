"""Class for handling all gamemodes and its functions"""
import player
import computer
import highscore


class Game():
    """Game class for all gamemodes"""
    def __init__(self):
        self.playing = True
        self.highscore = highscore.Highscore()

    def player_computer(self):
        """Game between player and computer"""
        print("Welcome to Player vs Computer\n")
        name = input("Please enter your name: ")
        player1 = player.Player(name)

        print(f"Welcome {player1.get_name()}! Choose difficulty for the" +
              " computer\n")

        input_error = True
        out_of_bounds = True
        while input_error:
            try:
                # Check if the input is out of bounds
                while out_of_bounds:
                    diff = int(input("(1) Normal\n(2) Hard\n(3) Extreme " +
                                     "(you wont win)\n---> "))
                    if (diff < 1 or diff > 3):
                        print("Invalid input - Try again!")
                        out_of_bounds = True
                    else:
                        out_of_bounds = False
            except ValueError:
                print("Invalid input - Try again!")
            else:
                input_error = False

        computer1 = computer.Computer(1, (6 * diff))

        while self.playing:
            self.player_move(player1)
            self.check_if_win(player1.get_score(), player1.get_name())

            computer1.stay_or_roll(self.playing)

            if computer1.get_score() >= 20:
                print("The computer wins with a score of " +
                      f"{computer1.get_score()}!")
                print("Game ended!")
                break

    def player_v_player(self):
        """Method for two players playing against eachother"""
        print("Welcome to Player vs Player!\n")

        name = input("Please enter Player 1 name: ")
        player1 = player.Player(name)

        name2 = input("Please enter Player 2 name: ")
        player2 = player.Player(name2)

        print(f"Welcome {player1.get_name()} and {player2.get_name()}")

        while self.playing:
            self.player_move(player1)
            self.check_if_win(player1.get_score(), player1.get_name())

            self.player_move(player2)
            self.check_if_win(player2.get_score(), player2.get_name())

    def player_move(self, player0, get_input=input):
        """Function for when the player moves"""
        round_score = 0
        while self.playing:
            print(f"\n--- {player0.get_name()}'s turn ---")

            choice = get_input("Roll or Hold?\n--> ")

            if choice.lower() == "roll":
                roll = player0.roll_dice()
                if roll == 1:
                    print(f"{player0.get_name()} rolled a {roll} and loses " +
                          "all points for this turn!")
                    round_score = 0
                    break
                else:
                    round_score += roll
                    print(f"{player0.get_name()} rolled a {roll} and now has" +
                          f" {player0.get_score() + round_score} points!\n")
                if player0.get_score() + round_score >= 20:
                    player0.add_score(round_score)
                    break

            elif choice.lower() == "hold":
                player0.add_score(round_score)
                print(f"{player0.get_name()} has secured " +
                      f"{player0.get_score()} points!")
                round_score = 0
                return True

            elif choice.lower() == "changename":
                new_name = input("Enter new name:\n--> ")
                player0.name = new_name

            elif choice.lower() == "quit":
                print("Quitting the match")
                self.playing = False
                return self.playing

            elif choice.lower() == "cheat":
                player0.add_score(20)
                break

    def check_if_win(self, score, player_name):
        """Checks if the player has won"""
        if score >= 20:
            print(f"{player_name} Wins with a score of {score}")
            print("Game ended!")
            self.highscore.add_highscore(
                player_name, score
            )
            self.playing = False
        return self.playing

    def get_input(self, text):
        """Method for input, makes it easier to test"""
        return input(text)
