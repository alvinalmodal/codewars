import unittest
from src.vowel_changer import change_vowels


class TestVowelChanger(unittest.TestCase):
    def test_change_vowels(self):
        self.assertEqual('hinnih hinnih bi-binnih binini finni fi-finnih fii, fy, mi-minnih. hinnih!', change_vowels("hannah hannah bo-bannah banana fanna fo-fannah fee, fy, mo-mannah. hannah!",'i') )
        self.assertEqual('odoro wonts to go to tho pork', change_vowels('adira wants to go to the park', 'o'))

    def test_change_vowels_if_sentence_is_not_a_string(self):
        with self.assertRaises(ValueError):
            change_vowels(12313,'a')

    def test_change_vowels_if_replacement_vowel_is_not_a_string(self):
        with self.assertRaises(ValueError):
            change_vowels('aeiou',1)

    def test_change_vowels_if_replacement_vowel_is_not_a_vowel(self):
        with self.assertRaises(ValueError):
            change_vowels('aeiou','b')


