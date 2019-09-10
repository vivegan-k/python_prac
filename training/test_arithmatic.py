import unittest 
from arithmatic import Arithmatic

class ArithmaticTest(unittest.TestCase):
    def setUp(self):
        self.ar_obj = Arithmatic(9,'hcl')
        
    def test_add(self):
        assert self.ar_obj.add() == 12

    def test_subtract(self):
        assert self.ar_obj.subtract() == 7

if __name__ == '__main__':
    unittest.main()
    
