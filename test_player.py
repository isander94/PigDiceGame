import unittest
from player import Player

"""Unittesting for player.py"""


class TestPlayerClass(unittest.TestCase):

    def setUp(self):
        """Setup for the tests"""
        self.myPlayer = Player("Galileo")

    def test_name(self):
        """Test so name is correct"""
        self.assertEqual(self.myPlayer.get_name(), "Galileo")

    def test_changeName(self):
        """Test so changing name works"""
        self.myPlayer.change_name("Aristoteles")
        self.assertEqual(self.myPlayer.get_name(), "Aristoteles")

    def test_getScore(self):
        """Tests so you can get a players score"""
        self.assertEqual(self.myPlayer.get_score(), 0)

    def test_addScore(self):
        """Tests so you can add score to a player"""
        self.myPlayer.add_score(5)
        self.assertEqual(self.myPlayer.get_score(), 5)

    def test_rollDice(self):
        """Tests so that the players dice only roll between 1 and 6"""
        diceRoll = self.myPlayer.roll_dice()
        expected = diceRoll >= 1 and diceRoll <= 6
        self.assertTrue(expected)
