import unittest
from src.converters.multiplier_converter import *
from base_converter_test_converter import *

class TestMultiplierConverter(unittest.TestCase, BaseCharacterConverter):
    inputs_and_outputs = [('a', 'aa'), ('1', '11'), ('a2', 'aa22'), ('1Aj2', '11AAjj22'), ('', '')]

    def converter(self):
        return multiplier_converter
    
if __name__ == '__main__':
    unittest.main()