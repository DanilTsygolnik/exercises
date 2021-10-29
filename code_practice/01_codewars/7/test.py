import unittest
from sol import array_plus_array

class Test(unittest.TestCase):

    def test_array_plus_array(self):
        with self.assertRaises(AssertionError):
            array_plus_array([],'123')
        with self.assertRaises(AssertionError):
            array_plus_array([], [1,2,'3',4])

        self.assertEqual(array_plus_array([], []), 0)
        self.assertEqual(array_plus_array([], [1]), 1)
        self.assertEqual(array_plus_array([1], [1]), 2)

if __name__=="__main__":
    unittest.main()
