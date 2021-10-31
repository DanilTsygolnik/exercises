import unittest
from sol import *

class Test(unittest.TestCase):

    def test_wrong_input(self):
        with self.assertRaises(TypeError):
            greet(1234)

    def test_output(self):
        self.assertEqual(greet("x"), "Hello, x how are you doing today?")

if __name__=="__main__":
    unittest.main()
