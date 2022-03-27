import unittest
from ex_3_sol_v3 import *

class TestSquare(unittest.TestCase):

    def test_map1x1(self):
        test_map = CompaignMap()
        test_square = Square(0,0,test_map)
        self.assertEqual(test_square.get_neighbors(), [])

    def test_map3x3(self):
        # top, bottom, left, right
        test_map = CompaignMap(3,3)
        test_square = Square(0,0,test_map)
        self.assertEqual(test_square.get_neighbors(), [[1,0], [0,1]])
        test_square = Square(1,1,test_map)
        self.assertEqual(test_square.get_neighbors(), [[0,1], [2,1], [1,0], [1,2]])


if __name__=="__main__":
    unittest.main()
