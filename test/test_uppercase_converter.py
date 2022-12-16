import unittest
from base_converter_test_converter import *
from src.converters.uppercase_converter import *

class TestUppercaseConverter(unittest.TestCase, BaseCharacterConverter):
    def test_canary(self):
        self.assertTrue(True)
          
    inputs_and_outputs = [('abc', 'ABC'), ('ABC', 'ABC'), ('aBc', 'ABC'), ('a1Z', 'A1Z'), ('', '')]
  
    def converter(self):
        return uppercase_converter

if __name__ == '__main__':
    unittest.main()