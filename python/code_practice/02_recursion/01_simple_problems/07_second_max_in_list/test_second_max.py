import unittest
from random import randint
from second_max import get_second_max

class TestFunc(unittest.TestCase):
 
    def test_main(self):
 
        self.assertIs(get_second_max([]), None)
        self.assertIs(get_second_max([1]), None)
        self.assertIs(get_second_max([1,1,1]), None)
        self.assertEqual(get_second_max([1,2,3]), 2)
        self.assertEqual(get_second_max([3,3,2,2,2,1]), 2)
        self.assertEqual(get_second_max([1,3,2,4]), 3)

if __name__=="__main__":
    unittest.main()
