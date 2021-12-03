import unittest
from random import randint
from even_indices import read_from_even

class TestFunc(unittest.TestCase):
 
    def test_main(self):
 
        self.assertEqual(read_from_even([]), [])
        self.assertEqual(read_from_even([0]), [0])
        self.assertEqual(read_from_even([0,1,2,3]), [0,2])
        self.assertEqual(read_from_even([0,1,2,3,4]), [0,2,4])

if __name__=="__main__":
    unittest.main()
