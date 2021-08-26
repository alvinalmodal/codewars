import unittest
from src.return_negative import make_negative


class TestReturnNegative(unittest.TestCase):
    def test_make_negative(self):
        self.assertEqual(-42, make_negative(42))
        self.assertEqual(-9, make_negative(9))
        self.assertEqual(0, make_negative(0))
        