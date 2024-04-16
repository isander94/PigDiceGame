
class Highscore:


    def __init__(self):
        """creates highscore list"""
        self.highscores = {}


    def add_highscore(self, name, highscore):
        """Save a highscore"""
        self.highscores[name] += highscore
        with open("highscore.txt", "a") as file:
            for player_name, score in self.highscores.items():
                file.write(f"{player_name} - {score}\n")

    