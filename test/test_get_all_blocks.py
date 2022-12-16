import unittest
import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname( __file__ ), os.pardir, 'src')))
from get_all_blocks import *

class TestGetAllBlocks(unittest.TestCase):
    def test_returns_a_none_empty_set(self): 
        blocks = getAllBlocks()
        self.assertTrue(blocks)

    def test_returns_a_set_that_includes_the_uppercase_converter(self):
        blocks = getAllBlocks()
        self.assertIn('uppercase_converter', blocks)
    
    def test_returns_a_set_that_includes_the_multiplier_converter(self):
        blocks = getAllBlocks()
        self.assertIn('multiplier_converter', blocks)

if __name__ == '__main__':
    unittest.main()