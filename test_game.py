import unittest
from game import Game


class testGameClass(unittest.TestCase):

    def setUp(self):
        self.g = Game()

    def test_checkWinner(self):
        """Checks if method for checking winner works,
        will return False if it works properply"""
        g = self.g.check_if_win(20, "galileo")
        self.assertFalse(g)
