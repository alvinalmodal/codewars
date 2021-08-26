import unittest
from src.generate_range_of_integers import generate_range


class TestGenerateRangeOfIntegers(unittest.TestCase):
    def test_generate_range(self):
        self.assertEqual([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], generate_range(1, 10, 1))
        self.assertEqual([-10, -9, -8, -7, -6, -5, -4, -3, -2, -1, 0, 1], generate_range(-10, 1, 1))

    def test_generate_range_invalid_min(self):
        with self.assertRaises(ValueError):
            generate_range('a', 10, 2)

    def test_generate_range_invalid_max(self):
        with self.assertRaises(ValueError):
            generate_range(1, 'a', 2)    

    def test_generate_range_invalid_step(self):
        with self.assertRaises(ValueError):
            generate_range(1, 10, 'a')    