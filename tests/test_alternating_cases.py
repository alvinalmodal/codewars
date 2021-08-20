import unittest
from src.alternating_cases import to_alternating_case


class TestAlternatingCases(unittest.TestCase):
    def test_alternating_cases_to_alternating_case(self):
        self.assertEqual('i AM aLVIN aLMODAL', to_alternating_case('I am Alvin Almodal'))
        self.assertEqual('cOUNT TO 123...', to_alternating_case('Count to 123...'))

    def test_alternating_cases_to_alternating_case_should_throw_an_error_when_input_is_invalid(self):
        with self.assertRaises(ValueError):
            to_alternating_case(12345)

