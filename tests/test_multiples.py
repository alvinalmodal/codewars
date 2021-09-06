import unittest
from src.multiples import multiple

class TestMultiples(unittest.TestCase):
    def test_multiple(self):
        self.assertEqual(multiple(30), "BangBoom")
        self.assertEqual(multiple(3), "Bang")
        self.assertEqual(multiple(98),"Miss")
        self.assertEqual(multiple(65),"Boom")
        self.assertEqual(multiple(23),"Miss")
        self.assertEqual(multiple(15),"BangBoom")

    def test_multiple_invalid_input_scenario(self):
        with self.assertRaises(ValueError):
            multiple('a')