from highscore import Highscore
import unittest

class TestHighscoreClass(unittest.TestCase):
    """Test for highscore class"""
    def setUp(self):
        """creating a setup for the tests"""
        self.highscore = Highscore()

    def test_add_highscore(self):
        """Tests the add_highscore method"""
        self.highscore.add_highscore("Galileo", 3)
        self.highscore.add_highscore("Aristoteles", 15)
        self.assertEqual(self.highscore.highscore_list,
                         {
                             "Galileo": 3,
                             "Aristoteles": 15
                         })
    
    def test_get_highscore(self):
        """Tests the get_highscore method"""
        self.highscore.add_highscore("Galileo", 3)
        self.highscore.add_highscore("Aristoteles", 15)
        highscores = self.highscore.get_highscore()
        self.assertEqual(
            highscores, {"Galileo ": 3, "Aristoteles ": 15}
        )