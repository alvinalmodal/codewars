import unittest
from src.even_or_odd import check_number


class TestEvenOrOdd(unittest.TestCase):
    def test_check_number(self):
        self.assertEqual("Even", check_number(2))
        self.assertEqual("Odd", check_number(3))
        self.assertEqual("Even", check_number(-2))
        self.assertEqual("Odd", check_number(-3))

    def test_check_number_invalid_input(self):
        with self.assertRaises(ValueError):
            check_number('-3')
            