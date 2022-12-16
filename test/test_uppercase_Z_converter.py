import unittest
from src.converters.uppercase_z_converter import *
from base_converter_test_converter import *

class TestUppercaseZConverter(unittest.TestCase, BaseCharacterConverter):
    inputs_and_outputs = [('Z', ''), ('z', 'z'), ('aZ', 'a'), ('A1Z2z', 'A12z'), ('', '')]

    def converter(self):
        return uppercase_z_converter
    
if __name__ == '__main__':
    unittest.main()