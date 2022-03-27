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


class TestCompaignMap(unittest.TestCase):

    def setUp(self):
        self.map_templ = CompaignMap()

    def test_indices_1x1(self):
        # get_squares_coord
        correct_indices = [[0,0]]
        test_indices = self.map_templ.get_squares_indices()
        # test grid formation
        self.assertEqual(correct_indices, test_indices)
        # test free squares number in a new grid
        self.assertEqual(len(test_indices), 1)

    def test_indices_3x2(self):
        correct_indices = [ [0,0], [0,1],
                            [1,0], [1,1],
                            [2,0], [2,1] ]
        test_indices = CompaignMap(3,2).get_squares_indices()
        # test grid formation
        self.assertEqual(correct_indices, test_indices)
        # test free squares number in a new grid
        self.assertEqual(len(test_indices), 6)

    def test_indices_2x3(self):
        correct_indices = [ [0,0], [0,1], [0,2],
                            [1,0], [1,1], [1,2] ]
        test_indices = CompaignMap(2,3).get_squares_indices()
        # test grid formation
        self.assertEqual(correct_indices, test_indices)
        # test free squares number in a new grid
        self.assertEqual(len(test_indices), 6)

    def test_square_access_by_indices(self):
        test_map = CompaignMap(3,3)
        test_square = test_map.grid[1][1]
        correct_neighbors_ind = [[0,1], [2,1], [1,0], [1,2]]
        self.assertEqual(test_square.get_neighbors(), correct_neighbors_ind)


if __name__=="__main__":
    unittest.main()
