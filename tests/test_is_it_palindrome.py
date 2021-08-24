import unittest
from src.is_it_palindrome import is_palindrome


class TestIsItPalindrome(unittest.TestCase):
    def test_is_palindrome(self):
        self.assertEqual(True, is_palindrome('a'))
        self.assertEqual(True, is_palindrome('aba'))
        self.assertEqual(True, is_palindrome('Abba'))
        self.assertEqual(True, is_palindrome('malam'))
        self.assertEqual(False, is_palindrome('walter'))
        self.assertEqual(True, is_palindrome('kodok'))
        self.assertEqual(False, is_palindrome('Kasue'))

    def test_is_palindrome_if_invalid_input(self):
        with self.assertRaises(ValueError):
            is_palindrome(123)