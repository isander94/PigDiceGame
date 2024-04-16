import cmd
import dice
import player
from game import Game

class GameLoop(cmd.Cmd):
    intro = "=== Pig Dice Game ===\n1] Player VS Computer - pvc\n2] Player VS Player - pvp\n3] High score\n4]\n5]"
    prompt = "--> "
    
    def do_quit(self, line):

        """Quits the program"""
        return True
    
    def do_menu(self, arg):
        """Shows game menu"""

        print("\n1] Player VS Computer - PVC\n2] Player VS Player - PVP\n3] High score\n4]\n5]")

    def do_pvc(self, arg):
        """Selects the game mode to play against the computer"""

        name = input("Enter name for player: ")
        player = player.Player(name)


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
    def do_startgame(self, arg):
        pass



# Start the game loop

if __name__ == '__main__':
    GameLoop().cmdloop()