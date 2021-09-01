import unittest
from src.all_inclusive import contain_all_rots

class TestAllInclusive(unittest.TestCase):
    def test_contain_all_rots(self):
        self.assertEqual(True, contain_all_rots("", ""))
        self.assertEqual(True, contain_all_rots("", ["bsjq", "qbsj"]))
        self.assertEqual(True, contain_all_rots("bsjq", ["bsjq", "qbsj", "sjqb", "twZNsslC", "jqbs"]))
        self.assertEqual(False, contain_all_rots("XjYABhR", ["TzYxlgfnhf", "yqVAuoLjMLy", "BhRXjYA", "YABhRXj", "hRXjYAB", "jYABhRX", "XjYABhR", "ABhRXjY"]))