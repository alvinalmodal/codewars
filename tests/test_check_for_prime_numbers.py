import unittest
from src.check_for_prime_numbers import is_prime


class TestCheckForPrimeNumbers(unittest.TestCase):
    def test_is_prime(self):
        self.assertEqual(is_prime(0), False)
        self.assertEqual(is_prime(1), False)
        self.assertEqual(is_prime(2), True)
        self.assertEqual(is_prime(3), True)
        self.assertEqual(is_prime(11), True)
        self.assertEqual(is_prime(12), False)
        self.assertEqual(is_prime(571), True)
        self.assertEqual(is_prime(25), False)

    def test_is_prime_with_invalid_input(self):
        with self.assertRaises(ValueError):
            is_prime("a")