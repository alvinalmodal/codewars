import unittest
from src.split_in_parts import split


class TestSplitInParts(unittest.TestCase):
    def test_split(self):
        self.assertEqual(split("supercalifragilisticexpialidocious", 3), "sup erc ali fra gil ist ice xpi ali doc iou s")
        self.assertEqual(split("HelloKata", 1), "H e l l o K a t a")
        self.assertEqual(split("HelloKata", 9), "HelloKata")