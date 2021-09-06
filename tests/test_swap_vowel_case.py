import unittest
from src.swap_vowel_case import swap_vowel_case as swap

class TestSwapVowelCase(unittest.TestCase):
    def test_swap_vowel(self):
        self.assertEqual(swap(" "), " ")
        self.assertEqual(swap("C Is AlIvE!"), "C is alive!")
        self.assertEqual(swap("to"), "tO")
        self.assertEqual(swap("The"), "ThE")

    def test_swap_vowel_invalid_input_case(self):
        with self.assertRaises(ValueError):
            swap(1)