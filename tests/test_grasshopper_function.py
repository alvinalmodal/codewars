import unittest
from src.grass_hopper_function import main


class TestGrasshopperFunction(unittest.TestCase):
    def test_grass_hopper_function_main(self):
        self.assertEqual('take item', main('take ', 'item'))
        self.assertEqual('use sword', main('use ', 'sword'))
    