import unittest
from src.thinkful_string_drills import quotable


class TestThinkfulStringDrills(unittest.TestCase):
    def test_quotable(self):
        self.assertEqual(quotable('Grae', 'Practice makes perfect'), 'Grae said: "Practice makes perfect"')
        self.assertEqual(quotable('Dan', 'Get back to work, Grae'), 'Dan said: "Get back to work, Grae"')
        self.assertEqual(quotable('Alex', 'Python is great fun'), 'Alex said: "Python is great fun"')
        self.assertEqual(quotable('Bethany', 'Yes, way more fun than R'), 'Bethany said: "Yes, way more fun than R"')
        self.assertEqual(quotable('Darrell', 'What the heck is this thing?'), 'Darrell said: "What the heck is this thing?"')

    def test_quotable_invalid_name(self):
        with self.assertRaises(ValueError):
            quotable(1,"2")

    def test_quotable_invalid_quote(self):
        with self.assertRaises(ValueError):
            quotable("test",1)