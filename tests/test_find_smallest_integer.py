import unittest
from src.find_smallest_integer import find_smallest_int


class TestFindSmallestInteger(unittest.TestCase):
    def test_find_smallest_int(self):
        self.assertEqual(11, find_smallest_int([30, 32, 1000, 11, 10000]))
        self.assertEqual(-32, find_smallest_int([30, -32, 1000, 11, 10000]))

    def test_find_smallest_int_should_return_error_if_invalid_input(self):
        with self.assertRaises(ValueError):
            find_smallest_int('alvin')