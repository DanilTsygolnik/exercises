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

    def test_lovefunc(self):
        self.assertTrue(lovefunc(1,2))
        self.assertTrue(lovefunc(2,1))
        self.assertFalse(lovefunc(2,2))
        self.assertFalse(lovefunc(1,1))
        # suggested
        self.assertIs(lovefunc(1,4), True)
        self.assertIs(lovefunc(2,2), False)
        self.assertIs(lovefunc(0,1), True)
        self.assertIs(lovefunc(0,0), False)

if __name__=="__main__":
    unittest.main()
