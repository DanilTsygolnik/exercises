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
        with self.assertRaises(AssertionError):
            lovefunc(0,1)
        with self.assertRaises(AssertionError):
            lovefunc(1,0)
        with self.assertRaises(AssertionError):
            lovefunc(0,0)

    def test_lovefunc(self):
        self.assertTrue(lovefunc(1,2))
        self.assertTrue(lovefunc(2,1))
        self.assertFalse(lovefunc(2,2))
        self.assertFalse(lovefunc(1,1))
        pass

if __name__=="__main__":
    unittest.main()
