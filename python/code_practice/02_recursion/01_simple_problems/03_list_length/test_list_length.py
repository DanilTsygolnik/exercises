import unittest
from random import randint
from list_length import get_length

class TestFunc(unittest.TestCase):
 
    def test_main(self):
 
        self.assertEqual(get_length([]), 0)

        rand_list = [1] * randint(1, 100)
        refer_length = len(rand_list)
        self.assertEqual(get_length(rand_list), refer_length)

if __name__=="__main__":
    unittest.main()
