import unittest
from src.your_a_square import is_square


class TestYourASquare(unittest.TestCase):
    def test_is_square(self):
        self.assertEqual(False, is_square(-1))
        self.assertEqual(True, is_square(0))
        self.assertEqual(False, is_square(3))
        self.assertEqual(True, is_square(4))
        self.assertEqual(True, is_square(25))
        self.assertEqual(False, is_square(26))

    def test_is_square_invalid_input(self):
        with self.assertRaises(ValueError):
            is_square('this is not a number')