import cmd
import dice
import player
from game import Game
import computer
import PvC

class GameLoop(cmd.Cmd):
    intro = "=== Pig Dice Game ===\nPlayer VS Computer - pvc\nPlayer VS Player - pvp\nHigh score\nQuit"
    prompt = "--> "
    
    def do_quit(self, line):

        """Quits the program"""
        return True
    
    def do_menu(self, arg):
        """Shows game menu"""

        print("\nPlayer VS Computer - PVC\nPlayer VS Player - PVP\nHigh score\nQuit")

    def do_pvc(self, arg):
        """Selects the game mode to play against the computer"""
        name = input("Enter name for player: ")
        player1 = player.Player(name)
        print("choose what difficulty \nNormal\nHard\nExtreme (you won't win)")
        difficulty = int(input("--> "))
        computer1 = computer.Computer(1, (6*difficulty))
        pvc_game = PvC(player1, computer1)


    def do_pvp(self, arg):
        """Selects the game mode for two players"""
        print("Starting a player versus player game!")
        name = input("Enter name of player 1: ")
        player1 = player.Player(name)
        name = input("Enter name of player 2: ")
        player2 = player.Player(name)
        pvp_game = Game(player1, player2)
        pvp_game.start()

    def do_highscore(self, arg):
        """Show the high score of previous games by players"""
        pass


if __name__ == '__main__':
    GameLoop().cmdloop()