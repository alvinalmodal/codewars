import unittest
from src.vaporcode import vaporize


class TestVaporCode(unittest.TestCase):
    def test_vaporize(self):
        self.assertEqual("L  E  T  S  G  O  T  O  T  H  E  M  O  V  I  E  S", vaporize("Lets go to the movies"))
        self.assertEqual("W  H  Y  I  S  N  '  T  M  Y  C  O  D  E  W  O  R  K  I  N  G  ?", vaporize("Why isn't my code working?"))

    def test_vaporize_if_invalid_input(self):
        with self.assertRaises(ValueError):
            vaporize(12314)