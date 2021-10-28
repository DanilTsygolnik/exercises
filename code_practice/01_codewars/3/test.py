import unittest
from sol import lovefunc

class Test(unittest.TestCase):

    def test_input_check(self):
        with self.assertRaises(AssertionError):
            lovefunc('1', 1)
        with self.assertRaises(AssertionError):
            lovefunc(1, '1')
        with self.assertRaises(AssertionError):
            lovefunc('1', '1')

    def test_(self):
        pass

if __name__=="__main__":
    unittest.main()
