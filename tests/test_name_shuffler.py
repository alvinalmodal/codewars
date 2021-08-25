import unittest
from src.name_shuffler import shuffle


class TestNameShuffler(unittest.TestCase):
    def test_shuffle(self):
        self.assertEqual("Alvin Almodal", shuffle('Almodal Alvin'))
        self.assertEqual("DericK Velez", shuffle("Velez DericK"))

    def test_shuffle_input_is_not_a_string(self):
        with self.assertRaises(ValueError):
            shuffle(1)