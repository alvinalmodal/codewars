import unittest
from src.remove_the_exclamation_marks import remove


class TestRemoveTheExclamationMarks(unittest.TestCase):
    def setUp(self):
        self.scenarios = [
                        #input, expected,
                        ["Hi!" , "Hi"],
                        ["Hi!!!" ,"Hi"],
                        ["!Hi" , "!Hi"],
                        ["!Hi!" , "!Hi"],
                        ["Hi! Hi!" , "Hi! Hi"],
                        ["Hi" , "Hi"],
                    ]

    def test_remove(self):
        for scenario in self.scenarios:
            self.assertEqual(scenario[1], remove(scenario[0])) 

    def test_remove_should_raise_error_if_invalid_input(self):
        with self.assertRaises(ValueError):
            remove(12345)
