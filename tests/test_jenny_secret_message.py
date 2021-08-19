import unittest
from src.jenny_secret_message import greet


class TestJennySecretMessage(unittest.TestCase):
    def test_greet(self):
        self.assertEqual("Hello Alvin!", greet('Alvin'))
        self.assertEqual("Hello Diane!", greet('Diane'))

    def test_greet_using_johnny(self):
        self.assertEqual("Hello, my love!", greet('Johnny'))