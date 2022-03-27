import unittest
from ex_3_sol_v2 import CompaignMap

class TestCompaignMap(unittest.TestCase):

    def setUp(self):
        self.map_templ = CompaignMap()

    def test_grid_1x1(self):
        correct_grid = [[[0,0,0]]]
        test_grid = self.map_templ
        # test grid formation
        self.assertEqual(correct_grid, test_grid.get_grid())
        # test free squares number in a new grid
        self.assertEqual(test_grid.get_num_free_squares(), 1)

    def test_grid_3x2(self):
        correct_grid = [ [[0,0,0], [0,1,0]],
                         [[1,0,0], [1,1,0]],
                         [[2,0,0], [2,1,0]] ]
        test_grid = CompaignMap(3,2)
        # test grid formation
        self.assertEqual(correct_grid, test_grid.get_grid())
        # test free squares number in a new grid
        self.assertEqual(test_grid.get_num_free_squares(), 3*2)

    def test_grid_2x3(self):
        correct_grid = [ [[0,0,0], [0,1,0], [0,2,0]],
                         [[1,0,0], [1,1,0], [1,2,0]] ]
        test_grid = CompaignMap(2,3)
        # test grid formation
        self.assertEqual(correct_grid, test_grid.get_grid())
        # test free squares number in a new grid
        self.assertEqual(test_grid.get_num_free_squares(), 2*3)

    def test_upd(self):
        # test upd_grid
        correct_grid = [ [[0,0,0], [0,1,0], [0,2,0]],
                         [[1,0,0], [1,1,0], [1,2,0]] ]
        self.map_templ.upd_grid(correct_grid)
        self.assertEqual(correct_grid, self.map_templ.get_grid())
        
        # test upd_num_free_squares
        self.map_templ.upd_num_free_squares(100)
        self.assertEqual(self.map_templ.get_num_free_squares(), 100)


if __name__=="__main__":
    unittest.main()
