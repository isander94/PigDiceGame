
class Highscore:

    def __init__(self):
        """creates highscore list"""
        self.highscore_list = {}

    def add_highscore(self, name, highscore):
        """Function that saves a players name and score after a victory"""
        # self.highscore_list[name] = highscore
        # with open("highscore.txt", "a") as file:
        #     for player_name, score in self.highscore_list.items():
        #         file.write(f"{player_name} - {score}\n")

        with open("highscore.txt", "a") as file:
            file.write(f"{name} - {highscore}")

    def show_highscore(self):
        """Function to print names and their highscores"""
        # self.highscore_list = {}
        # with open("highscore.txt","r") as file:
        #     for line in file:
        #         name, score = line.strip().split("-")
        #         self.highscore_list[name] = int(score)
        
        # Start reading from file
        with open("highscore.txt", "r") as file:
            for x in range(20):
                print("*", end="")
            print()

            for line in file:
                name, score = line.strip().split("-")
                print(f"{name:10}{score:>10}")
            
            for x in range(20):
                print("*", end="")
            print()
        
        # Remove this line later?
        # return self.highscore_list
    
    def print_highscore(self, highscore_list):
        print(highscore_list)
    