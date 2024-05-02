"""Class that handles the highscore list"""


class Highscore:
    """creates highscore list"""
    def __init__(self):
        self.highscore_list = {}

    def add_highscore(self, name, highscore):
        """Function that saves a players name and score after a victory"""
        with open("highscore.txt", "a", encoding="utf-8") as file:
            file.write(f"{name} - {highscore}")

    def show_highscore(self):
        """Function to print names and their highscores"""

        # Start reading from file
        with open("highscore.txt", "r", encoding="utf-8") as file:
            for x in range(20):
                print("*", end="")
            print()

            for line in file:
                name, score = line.strip().split("-")
                print(f"{name:10}{score:>10}")

            for x in range(20):
                print("*", end="")
            print()

    def print_highscore(self, highscore_list):
        """Function for printing highscore list"""
        print(highscore_list)
