import unittest
from sol import get_smallest_v1
from sol import get_smallest_v2

class Test(unittest.TestCase):
    def setUp(self):
        self.arrays = [
                        [34, 15, 88, 2], 
                        [34, -345, -1, 100]
                      ]
        self.answers = [2, -345]

    def test_get_smallest(self):
        for i, _ in enumerate(self.answers):
            self.assertEqual(get_smallest_v1(self.arrays[i]), self.answers[i])
            self.assertEqual(get_smallest_v2(self.arrays[i]), self.answers[i])

if __name__=="__main__":
    unittest.main()
