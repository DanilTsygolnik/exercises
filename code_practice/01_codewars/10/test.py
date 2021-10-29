import unittest
from sol import reverse_seq

class Test(unittest.TestCase):

    def test_reverse_seq(self):
        with self.assertRaises(TypeError):
            reverse_seq(4.3)
        with self.assertRaises(ValueError):
            reverse_seq(0)
        with self.assertRaises(ValueError):
            reverse_seq(-1)

        self.assertEqual(reverse_seq(1), [1])
        self.assertEqual(reverse_seq(2), [2,1])
        self.assertEqual(reverse_seq(3), [3,2,1])

if __name__=="__main__":
    unittest.main()
