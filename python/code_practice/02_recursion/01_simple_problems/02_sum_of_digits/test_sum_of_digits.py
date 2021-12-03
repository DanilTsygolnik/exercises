import unittest
from random import randint
from sum_of_digits import get_digits_sum

class TestFunc(unittest.TestCase):
 
    def test_main(self):
 
        self.assertEqual(get_digits_sum(0), 0)

        rand_num = randint(1, 10000)
        refer_int = 0
        for c in str(rand_num):
            refer_int += int(c)
        self.assertEqual(get_digits_sum(rand_num), refer_int)

if __name__=="__main__":
    unittest.main()
