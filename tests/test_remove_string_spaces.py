import unittest
from src.remove_string_spaces import no_space


class TestRemoveStringSpaces(unittest.TestCase):
    def test_no_space(self):
        self.assertEqual('8j8mBliB8gimjB8B8jlB', no_space('8 j 8   mBliB8g  imjB8B8  jl  B'))
        self.assertEqual('88Bifk8hB8BB8BBBB888chl8BhBfd', no_space('8 8 Bi fk8h B 8 BB8B B B  B888 c hl8 BhB fd'))
        self.assertEqual('8aaaaaddddr', no_space('8aaaaa dddd r     '))
        self.assertEqual('jfBmgklf8hg88lbe8', no_space('jfBm  gk lf8hg  88lbe8 ')) 
        self.assertEqual('8jaam', no_space('8j aam'))
        