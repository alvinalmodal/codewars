import unittest
from src.reverse_words import reverse


class TestReverseWords(unittest.TestCase):
    def test_reverse_words(self):
        self.assertEqual("battle no requires which that is victory greatest The", reverse("The greatest victory is that which requires no battle"))
        self.assertEqual("world! Hello", reverse("Hello world!"))

    def test_reverse_words_should_raise_error_if_invalid_input(self):
        with self.assertRaises(ValueError):
            reverse(12345)