"""Unit testing for dice class"""
import unittest
from dice import Dice


class TestDiceClass(unittest.TestCase):
    """Setting up with dice class, and testing it"""
    def setUp(self):
        self.my_dice = Dice(1, 10)

    def test_roll_dice(self):
        """Rolls the dice, and checks if it's between 1 and 10"""
        rolled_number = self.my_dice.roll_dice()
        expected = rolled_number >= 1 and rolled_number <= 10
        self.assertTrue(expected)

    def test_low_number(self):
        """Checks that the lowest number on the die is 1"""
        expected_low = 1
        self.assertEqual(expected_low, self.my_dice.low)

    def test_high_number(self):
        """Checks that the highest number on the die is 10"""
        expected_high = 10
        self.assertEqual(expected_high, self.my_dice.high)

    def test_return(self):
        """Checks so that roll_dice actually returns something"""
        number = self.my_dice.roll_dice()
        self.assertIsNotNone(number)


if __name__ == "__main__":
    unittest.main()
