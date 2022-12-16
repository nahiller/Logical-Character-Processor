import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname( __file__ ), os.pardir, 'src')))
from src.get_converters import *
from src.converters import uppercase_z_converter, uppercase_converter, lowercase_converter
import unittest

class TestGetConverters(unittest.TestCase):
    def test_empty_list_returns_empty_list(self):
        self.assertFalse(get_converters([]))

    def test_list_with_uppercase_z_converter_as_string_returns_list_with_correct_function(self):
        result = get_converters(['uppercase_z_converter'])
        self.assertIn(uppercase_z_converter.uppercase_z_converter, result)
    
    def test_list_with_uppercase_converter_as_string_returns_list_with_correct_functions(self):
        result = get_converters(['uppercase_converter'])
        self.assertIn(uppercase_converter.uppercase_converter, result)

    def test_list_with_uppercase_converter_and_uppercase_z_converter_as_strings_returns_list_without_lowercase_converter(self):
        result = get_converters(['uppercase_converter', 'uppercase_z_converter'])
        self.assertNotIn(lowercase_converter.lowercase_converter, result)
    
    def test_list_with_uppercase_converter_and_uppercase_z_converter_as_strings_returns_correct_list(self):
        result = get_converters(['uppercase_converter', 'uppercase_z_converter'])
        self.assertEqual([uppercase_converter.uppercase_converter, uppercase_z_converter.uppercase_z_converter], result)