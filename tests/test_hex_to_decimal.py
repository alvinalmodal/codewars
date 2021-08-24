import unittest
from src.hex_to_decimal import hex_to_dec


class TestHexToDecimal(unittest.TestCase):
    def test_hex_to_dec(self):
        self.assertEqual(1, hex_to_dec("1"))
        self.assertEqual(10, hex_to_dec("a"))
        self.assertEqual(16, hex_to_dec("10"))

    def test_hex_to_dec_invalid_input(self):
        with self.assertRaises(ValueError):
            hex_to_dec(13)