import unittest
from sol import fiter
from sol import twice_as_old

class Test(unittest.TestCase):

    def test_twice_as_old(self):

        with self.assertRaises(AssertionError):
            twice_as_old(6,6)

        self.assertEqual(twice_as_old(6,2), 2)
        self.assertEqual(twice_as_old(4,2), 0)
        self.assertEqual(twice_as_old(5,3), 1)
        self.assertEqual(twice_as_old(7,5), 3)
        self.assertEqual(twice_as_old(9,5), 1)
        self.assertEqual(twice_as_old(7,3), 1)
        self.assertEqual(twice_as_old(6,2), 2)
        self.assertEqual(twice_as_old(6,3), 0)
        self.assertEqual(twice_as_old(8,3), 2)
        self.assertEqual(twice_as_old(8,5), 2)
        self.assertEqual(twice_as_old(7,4), 1)
        self.assertEqual(twice_as_old(9,4), 1)
        self.assertEqual(twice_as_old(9,0), 9)
        self.assertEqual(twice_as_old(6,2), 2)
        self.assertEqual(twice_as_old(10,6), 2)


if __name__=="__main__":
    unittest.main()
