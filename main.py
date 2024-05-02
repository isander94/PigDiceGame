"""Main class for handling gameloop"""
import cmd
from game import Game
import highscore


class GameLoop(cmd.Cmd):
    """Main Gameloop"""
    intro = "=== Pig Dice Game ===\nType 'help' to show commands"
    prompt = "--> "

    def do_quit(self, line):
        """Quits the program"""
        return True

    def do_menu(self, arg):
        """Shows game menu"""
        print("\n      Option          Command   \n" +
              "|------------------|-----------|\n" +
              "|Player VS Computer|    pvc    |\n" +
              "|------------------|-----------|\n" +
              "| Player VS Player |    pvp    |\n" +
              "|------------------|-----------|\n" +
              "|     Highscore    | highscore |\n" +
              "|------------------|-----------|\n" +
              "|      Rules       |   rules   |\n" +
              "|------------------|-----------|\n" +
              "|   Quit program   |   quit    |\n" +
              " ------------------------------")

    def do_pvc(self, arg):
        """Selects the game mode to play against the computer"""
        Game().player_computer()
        self.do_menu(arg)

    def do_pvp(self, arg):
        """Selectes gamemode Player vs Player"""
        Game().player_v_player()
        self.do_menu(arg)

    def do_highscore(self, arg):
        """Show the high score of previous games by players"""
        high = highscore.Highscore()
        high.show_highscore()
        self.do_menu(arg)

    def do_rules(self, arg):
        """Displays the rules of the game"""
        print(
            """\n
              Each turn a player gets to roll their dice as
              many times as they want, accumulating all points they get
              along the way. However if you roll a 1, you lose all your
              points you have gathered on that turn. Therefore it could be
              wise to hold on to your points after a few rolls.

              After the first player has either rolled a 1, or has decided to
              stay with their points, the turn goes over to the next player.

              This goes on until someone reaches 100 points first

              Good luck!""")


if __name__ == '__main__':
    GameLoop().cmdloop()
