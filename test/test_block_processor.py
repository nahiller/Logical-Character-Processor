import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname( __file__ ), os.pardir, 'src')))
import unittest
from block_processor import *
from src.converters import uppercase_converter, lowercase_converter, multiplier_converter, uppercase_z_converter

class TestBlockProcessor(unittest.TestCase):
    def test_no_block(self):
        processed_text = blockProcessor('aBc')
        self.assertEqual('aBc', processed_text)
    
    def test_uppercase_converter(self):
        processed_text = blockProcessor('aBc', uppercase_converter.uppercase_converter)
        self. assertEqual('ABC', processed_text)

    def test_lowercase_converter(self):
        processed_text = blockProcessor('aBc', lowercase_converter.lowercase_converter)
        self.assertEqual('abc', processed_text)
    
    def test_uppercase_multiplier(self):
        processed_text = blockProcessor('aBc', uppercase_converter.uppercase_converter, multiplier_converter.multiplier_converter)
        self.assertEqual('AABBCC', processed_text)
    
    def test_uppercase_multiplier_lowercase(self):
        processed_text = blockProcessor('aBc', uppercase_z_converter.uppercase_z_converter, multiplier_converter.multiplier_converter, lowercase_converter.lowercase_converter)
        self.assertEqual('aabbcc', processed_text)

if __name__ == '__main__':
    unittest.main()