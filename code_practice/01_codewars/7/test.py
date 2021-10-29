import unittest
from sol import arr_elem_sum
from sol import array_plus_array

class Test(unittest.TestCase):

    def test_arr_elem_sum(self):
        with self.assertRaises(AssertionError):
            arr_elem_sum('123')
        with self.assertRaises(AssertionError):
            arr_elem_sum([1,2,'3',4])

        self.assertEqual(arr_elem_sum([]), 0)
        self.assertEqual(arr_elem_sum([1]), 1)
        self.assertEqual(arr_elem_sum([1,1]), 2)

    def test_array_plus_array(self):
        self.assertEqual(array_plus_array([], [1]), 1)
        self.assertEqual(array_plus_array([1], [1]), 2)

if __name__=="__main__":
    unittest.main()
