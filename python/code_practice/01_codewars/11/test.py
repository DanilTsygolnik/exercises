import unittest
from sol import other_angle

class Test(unittest.TestCase):

    def test_input(self):
        with self.assertRaises(ValueError):
            other_angle(10,170)

    def test_output(self):
        self.assertEqual(other_angle(30, 60), 90)
        self.assertEqual(other_angle(60, 60), 60)
        self.assertEqual(other_angle(43, 78), 59)
        self.assertEqual(other_angle(10, 20), 150)

if __name__=="__main__":
    unittest.main()
