import unittest
from src.ensure_question import ensure


class TestEnsureQuestion(unittest.TestCase):
    def test_ensure(self):
        self.assertEqual(ensure(""),"?")
        self.assertEqual(ensure("Yes"),"Yes?")
        self.assertEqual(ensure("No?"),"No?")
        self.assertEqual(ensure("Well????"),"Well????")

