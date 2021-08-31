import unittest
from src.convert_boolean_to_string import boolean_to_string


class TestConvertBooleanToString(unittest.TestCase):
    def test_boolean_to_string(self):
        self.assertEqual("True", boolean_to_string(True))
        self.assertEqual("False", boolean_to_string(False))

    def test_boolean_to_string_invalid_input(self):
        with self.assertRaises(ValueError):
            boolean_to_string(123)