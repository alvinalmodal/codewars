import unittest
from src.is_it_a_number import is_digit


class TestIsItANumber(unittest.TestCase):
    def test_is_digit(self):
        self.assertEqual(False, is_digit('s234'))
        self.assertEqual(True, is_digit(4))
        self.assertEqual(True, is_digit("3"))
        self.assertEqual(True , is_digit('   3   '))
        self.assertEqual(False, is_digit('   3   5'))
        self.assertEqual(True, is_digit('-234.4'))