import unittest
from src.fundamentals_return import add, subt, multiply, divide, mod, exponent


class TestFundamentalsReturn(unittest.TestCase):
    def test_add(self):
        self.assertEqual(12, add(4,3,5))

    def test_add_invalid_input(self):
        with self.assertRaises(ValueError):
            add(4,5,3,'a')

    def test_subt(self):
        self.assertEqual(12, subt(22,10))

    def test_subt_invalid_input(self):
        with self.assertRaises(ValueError):
            subt('a', 3)

    def test_multiply(self):
        self.assertEqual(12, multiply(6, 2))

    def test_multiply_invalid_input(self):
        with self.assertRaises(ValueError):
            multiply('a', 'b')

    def test_divide(self):
        self.assertEqual(2.5, divide(5,2))

    def test_divide_invalid_input(self):
        with self.assertRaises(ValueError):
            divide(2.5,'x')

    def test_mod(self):
        self.assertEqual(0, mod(8, 2))
        self.assertEqual(1, mod(3, 2))

    def test_mod_invalid_input(self):
        with self.assertRaises(ValueError):
            mod(3, '1')

    def test_exponent(self):
        self.assertEqual(4, exponent(2, 2))

    def test_exponent_invalid_input(self):
        with self.assertRaises(ValueError):
            exponent('a', 'b')