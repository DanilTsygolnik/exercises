import unittest
from random import randint
from even_only import get_only_even

class TestFunc(unittest.TestCase):
 
    def test_main(self):
 
        self.assertEqual(get_only_even([]), [])
 
        rand_numbers = list(range(-100, 101, 1))
        even_refer = []
        for i in rand_numbers:
            if i % 2 == 0:
                even_refer.append(i)
        self.assertEqual(get_only_even(rand_numbers), even_refer)

if __name__=="__main__":
    unittest.main()
