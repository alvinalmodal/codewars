import unittest
from src.sort_and_star import two_sort


class TestSortAndStar(unittest.TestCase):
    def test_two_sort(self):
        self.assertEqual('b***i***t***c***o***i***n', two_sort(["bitcoin", "take", "over", "the", "world", "maybe", "who", "knows", "perhaps"]))
        self.assertEqual('a***r***e', two_sort(["turns", "out", "random", "test", "cases", "are", "easier", "than", "writing", "out", "basic", "ones"]))
        self.assertEqual('a***b***o***u***t', two_sort(["lets", "talk", "about", "javascript", "the", "best", "language"]))
        self.assertEqual('c***o***d***e', two_sort(["i", "want", "to", "travel", "the", "world", "writing", "code", "one", "day"]))
        self.assertEqual('L***e***t***s', two_sort(["Lets", "all", "go", "on", "holiday", "somewhere", "very", "cold"]))
