import unittest
from src.previous_multiple_of_three import prev_mult_of_three


class TestPreviousMultipleOfThree(unittest.TestCase):
    def test_prev_mult_of_three(self):
        self.assertEqual(prev_mult_of_three(1), None)
        self.assertEqual(prev_mult_of_three(25), None)
        self.assertEqual(prev_mult_of_three(36), 36)
        self.assertEqual(prev_mult_of_three(1244), 12)
        self.assertEqual(prev_mult_of_three(952406), 9)

    def test_prev_mult_of_three_invalid_input(self):
        with self.assertRaises(ValueError):
            prev_mult_of_three("123a")