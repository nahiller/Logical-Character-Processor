import unittest
from src.converters.lowercase_converter import *
from base_converter_test_converter import *

class TestLowercaseConverter(unittest.TestCase, BaseCharacterConverter):
    inputs_and_outputs = [('ABC', 'abc'), ('abc', 'abc'), ('aBc', 'abc'), ('A1Z', 'a1z'), ('', '')]

    def converter(self):
        return lowercase_converter
    
if __name__ == '__main__':
    unittest.main()