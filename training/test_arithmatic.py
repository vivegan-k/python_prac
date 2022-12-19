import imp
import unittest 
from unittest.mock import patch
from arithmatic import Arithmatic

class ArithmaticTest(unittest.TestCase):
    def setUp(self):
        self.ar_obj = Arithmatic(9,3)
        
    def test_add(self):
        assert self.ar_obj.add() == 12

    def test_subtract(self):
        assert self.ar_obj.subtract() == 6

    @patch('arithmatic.Arithmatic.multiply')
    def test_add_mock(self, multiply_mock):
        multiply_mock.return_value = 12
        assert self.ar_obj.multiply(5,4) == 12
        multiply_mock.assert_called_with(5,4)
        





if __name__ == '__main__':
    unittest.main()
    
# For unittest

def test_add():
   c = 1 + 2 

