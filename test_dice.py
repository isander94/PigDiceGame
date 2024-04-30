import unittest
from dice import Dice

"""Unit testing for dice class"""


class TestDiceClass(unittest.TestCase):

    def setUp(self):
        self.myDice = Dice(1, 10)

    def test_roll_dice(self):
        """Rolls the dice, and checks if it's between 1 and 10"""
        rolled_number = self.myDice.roll_dice()
        expected = rolled_number >= 1 and rolled_number <= 10
        self.assertTrue(expected)

    def test_low_number(self):
        """Checks that the lowest number on the die is 1"""
        expected_low = 1
        self.assertEqual(expected_low, self.myDice.low)

    def test_high_number(self):
        """Checks that the highest number on the die is 10"""
        expected_high = 10
        self.assertEqual(expected_high, self.myDice.high)

    def test_return(self):
        number = self.myDice.roll_dice()
        self.assertIsNotNone(number)


if __name__ == "__main__":
    unittest.main()
