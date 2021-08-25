import unittest
from src.count_positive_and_sum_negative import count_positives_sum_negatives


class TestCountPositiveAndSumNegative(unittest.TestCase):
    def test_count_positives_sum_negatives(self):
        self.assertEqual([10, -65], count_positives_sum_negatives([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, -11, -12, -13, -14, -15]))
        self.assertEqual([8,-50], count_positives_sum_negatives([0, 2, 3, 0, 5, 6, 7, 8, 9, 10, -11, -12, -13, -14]))
        self.assertEqual([1, 0], count_positives_sum_negatives([1]))
        self.assertEqual([0,0], count_positives_sum_negatives([0,0,0,0,0,0,0,0,0]))
        self.assertEqual([], count_positives_sum_negatives([]))
