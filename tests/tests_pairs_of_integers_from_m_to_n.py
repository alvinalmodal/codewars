import unittest
from src.pairs_of_integers_from_m_to_n import generate_pairs

class TestPairsOfIntegersFromMtoN(unittest.TestCase):
    def test_generate_pairs(self):
        self.assertEquals(generate_pairs(2, 4),  [ (2, 2), (2, 3), (2, 4), (3, 3), (3, 4), (4, 4) ])
        self.assertEquals(generate_pairs(0, 1),  [ (0, 0), (0, 1), (1, 1) ])
        self.assertEquals(generate_pairs(0, 0),  [ (0, 0) ])

    def test_generate_pairs_invalid_m_case(self):
        with self.assertRaises(ValueError):
            generate_pairs('a', 3)

    def test_generate_pairs_invalid_n_case(self):
        with self.assertRaises(ValueError):
            generate_pairs(1, 'b')