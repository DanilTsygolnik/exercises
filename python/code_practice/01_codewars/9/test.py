import unittest
from sol import make_negative

class Test(unittest.TestCase):

    def test_make_negative(self):
        with self.assertRaises(TypeError):
            make_negative('123')
        self.assertEqual(make_negative(0), 0)
        self.assertEqual(make_negative(1), -1)
        self.assertEqual(make_negative(-1), -1)
        self.assertEqual(make_negative(1.1), -1.1)
        self.assertEqual(make_negative(-1.1), -1.1)

if __name__=="__main__":
    unittest.main()
