import cmd
from game import Game
import highscore


class GameLoop(cmd.Cmd):
    intro = "=== Pig Dice Game ===\nType 'help' to show commands"
    prompt = "--> "

    def do_quit(self, line):
        """Quits the program"""
        return True

    def do_menu(self, arg):
        """Shows game menu"""
        print("      Option          Command   \n" +
              "|------------------|-----------|\n" +
              "|Player VS Computer|    pvc    |\n" +
              "|------------------|-----------|\n" +
              "| Player VS Player |    pvp    |\n" +
              "|------------------|-----------|\n" +
              "|     Highscore    | highscore |\n" +
              "|------------------|-----------|\n" +
              "|   Quit program   |   quit    |\n" +
              " ------------------------------")

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
