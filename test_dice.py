import unittest
from dice import Dice

"""Unit testing for dice class"""

class TestDiceClass(unittest.TestCase):

    def test_roll_dice(self):
        """Rolls the dice, and checks if it's between 1 and 6"""
        myDice = Dice()
        rolled_number = myDice.roll_dice()
        expected = rolled_number >= 1 and rolled_number <= 6
        self.assertTrue(expected)

    def test_low_number(self):
        """Checks that the lowest number on the die is 1"""
        myDice = Dice()
        expected_low = 1
        self.assertEqual(expected_low, myDice.low)

    def test_high_number(self):
        """Checks that the highest number on the die is 6"""
        myDice = Dice()
        expected_high = 6
        self.assertEqual(expected_high, myDice.high)        

    def test_return(self):
        myDice = Dice()
        number = myDice.roll_dice()
        self.assertIsNotNone(number)

if __name__ == "__main__":
    unittest.main()