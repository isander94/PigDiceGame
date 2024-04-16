
class Highscore:


    def __init__(self):
        """creates highscore list"""
        self.highscore_list = {}


    def add_highscore(self, name, highscore):
        """Save a highscore"""
        self.highscore_list[name] += highscore
        with open("highscore.txt", "a") as file:
            for player_name, score in self.highscore_list.items():
                file.write(f"{player_name} - {score}\n")

    def get_highscore(self):
        """function to get names and their highscores"""
        self.highscore_list = {}
        with open("highscore.txt","r") as file:
            for line in file:
                name, score = line.strip().split("-")
                self.highscore_list[name] = int(score)
        return self.highscore_list
    