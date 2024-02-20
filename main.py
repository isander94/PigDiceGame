import cmd

class GameLoop(cmd.Cmd):
    intro = "=== Pig Dice Game ==="   
    prompt = "--> "
    
    def do_quit(self, line):
        """Quits the program"""
        return True
    
    def do_greet(self, arg):
        """Simply prints hello to the screen"""
        print("Hello, there!")

    def do_showmenu(self, arg):
        """Shows game menu"""
        print("This is the menu of the game\nYou can choose to show the menu at any time")

# Start the game loop

if __name__ == '__main__':
    GameLoop().cmdloop()