import unittest
from src.converters.lowercase_z_converter import *
from base_converter_test_converter import *

class TestLowerkConverter(unittest.TestCase, BaseCharacterConverter):
    inputs_and_outputs = [('z', ''), ('a', 'a'), ('az', 'a'), ('A1K2z', 'A1K2'), ('', '')]

    def converter(self):
        return lowercase_z_converter
    
if __name__ == '__main__':
    unittest.main()