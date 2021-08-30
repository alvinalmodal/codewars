import unittest
from src.how_do_i_compare_numbers import what_is


class TestHowDoICompareNumbers(unittest.TestCase):
    def test_what_is(self):
        tests = [
            (0, 'nothing'),
            (123, 'nothing'),
            (-1, 'nothing'),
            (42, 'everything'),
            (42 * 42, 'everything squared')
        ]
        for number, answer in tests:
            self.assertEqual(what_is(number), answer)