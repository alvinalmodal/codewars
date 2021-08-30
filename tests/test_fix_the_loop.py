import unittest
from src.fix_the_loop import list_animals


class TestFixTheLoop(unittest.TestCase):
    def test_list_animals(self):
        animals = [
            'dog',
            'cat',
            'elephant'
        ]
        self.assertEqual(list_animals(animals), '1. dog\n2. cat\n3. elephant\n')

    def test_list_animals_input_not_a_list(self):
        with self.assertRaises(ValueError):
            list_animals(1)