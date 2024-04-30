import cmd
import dice
import player
from game import Game
import computer
import highscore

class GameLoop(cmd.Cmd):
    intro = "==== Pig Dice Game ====\nPlayer VS Computer - pvc\nPlayer VS Player - pvp\nHigh score\nQuit program - quit"
    prompt = "--> "
    
    def do_quit(self, line):
        """Quits the program"""
        return True
    
    def do_menu(self, arg):
        """Shows game menu"""
        print("\nPlayer VS Computer - pvc\nPlayer VS Player - pvp\nHigh score\nQuit program - quit")

    def do_pvc(self, arg):
        """Selects the game mode to play against the computer"""
        Game().Player_Computer()
        self.do_menu(arg)


    def do_pvp(self, arg):
        """Selectes gamemode Player vs Player"""
        Game().Player_v_Player()
        self.do_menu(arg)

    def do_highscore(self, arg):
        """Show the high score of previous games by players"""
        high = highscore.Highscore()
        print(high.get_highscore())
        self.do_menu(arg)


if __name__ == '__main__':
    GameLoop().cmdloop()