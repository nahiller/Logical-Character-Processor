import unittest
from src.converters.letter_block_converter import *

class TestLetterBlockConverter(unittest.TestCase):
    def test_blank_letter_block_aBc_returns_aBc(self):
        result = letter_block_converter('')('aBc')
        self.assertEqual('aBc', result)

    def test_uppercase_b_turns_aBc_to_ac(self):
        result = letter_block_converter('B')('aBc')
        self.assertEqual('ac', result)

    def test_lowercase_a_turns_aBc_to_Bc(self):
        result = letter_block_converter('a')('aBc')
        self.assertEqual('Bc', result)

    def test_lowercase_z_turns_aBc_to_aBc(self):
        result = letter_block_converter('z')('aBc')
        self.assertEqual('aBc', result)
    
    def test_string_abc_returns_exception_blocker_must_be_a_single_letter(self):
        self.assertRaisesRegex(Exception, 'must be a single letter', letter_block_converter, 'gh')
