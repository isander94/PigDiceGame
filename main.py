import cmd
import dice
import player
from game import Game
import computer
import highscore

class GameLoop(cmd.Cmd):
    intro = "=== Pig Dice Game ===\n1] Player VS Computer - pvc\n2] Player VS Player - pvp\n3] High score\n4] Quit program - quit\n5]"
    prompt = "--> "
    
    def do_quit(self, line):
        """Quits the program"""
        return True
    
    def do_menu(self, arg):
        """Shows game menu"""
        print("\n1] Player VS Computer - pvc\n2] Player VS Player - pvp\n3] High score\n4] Quit program - quit\n5]")

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

    def do_startgame(self, arg):
        pass



if __name__ == '__main__':
    GameLoop().cmdloop()