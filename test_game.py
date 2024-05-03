"""unittest for game class"""
import unittest
from unittest.mock import patch
from game import Game
from player import Player


class TestGameClass(unittest.TestCase):
    """Setting up game class and testing it"""
    def setUp(self):
        self.g = Game()
        self.p = Player("Galileo")

    def test_check_winner(self):
        """Checks if method for checking winner works,
        will return False if it works properply"""
        g = self.g.check_if_win(20, "galileo")
        self.assertFalse(g)

    def test_check_not_winner(self):
        """Same method check but this time
        checks that the player hasn't won, will return True
        if it works properly"""
        g = self.g.check_if_win(15, "galileo")
        self.assertTrue(g)

    @patch('game.Game.get_input', return_value='hold')
    def test_player_move(self, input):
        """Test player_move method, see so user input works"""
        self.assertTrue(self.g.player_move(self.p, input))


if __name__ == "__main__":
    unittest.main()
