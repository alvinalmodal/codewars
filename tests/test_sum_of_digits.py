import unittest
from src.sum_of_digits import sum_digits

class TestSumOfDigits(unittest.TestCase):
    def test_sum_digits_string_test_case(self):
        self.assertEqual(sum_digits("3433"), "3 + 4 + 3 + 3 = 13")
        self.assertEqual(sum_digits("64323"), "6 + 4 + 3 + 2 + 3 = 18")
        self.assertEqual(sum_digits("8"), "8 = 8")

    def test_sum_digits_number_test_case(self):
        self.assertEqual(sum_digits(3433), "3 + 4 + 3 + 3 = 13")
        self.assertEqual(sum_digits(64323), "6 + 4 + 3 + 2 + 3 = 18")
        self.assertEqual(sum_digits(8), "8 = 8")

    def test_sum_digits_none_case(self):
        self.assertEquals(sum_digits(None), "")
        