import unittest
from src.words_to_sentence import sentence_converter


class TestWordsToSentence(unittest.TestCase):
    def test_sentence_converter(self):
        self.assertEqual('bacon is delicious', sentence_converter(['bacon', 'is', 'delicious']))

    def test_sentence_converter_invalid_input(self):
        with self.assertRaises(ValueError):
            sentence_converter(123)