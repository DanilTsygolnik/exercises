import unittest
import ex_18_sol

class Test_ex_18_sol(unittest.TestCase):

    def test_is_sort(self):
        
        self.assertTrue(ex_18_sol.is_sort([0, 0, 0, 0]))
        self.assertTrue(ex_18_sol.is_sort([1, 2, 2, 3]))
        self.assertTrue(ex_18_sol.is_sort([1, 2, 3, 4]))

    def test_get_rotated(self):
        
        test_list = [1, 1, 1, 2, 3, 4, 1, 1, 1]
        rot_one = ex_18_sol.get_rotated(test_list, 3)
        self.assertEqual(rot_one, [1, 1, 1, 3, 4, 2, 1, 1, 1])
        rot_two = ex_18_sol.get_rotated(rot_one, 3)
        self.assertEqual(rot_two, [1, 1, 1, 4, 2, 3, 1, 1, 1])
        rot_last = ex_18_sol.get_rotated(rot_two, 3)
        self.assertEqual(rot_last, [1, 1, 1, 2, 3, 4, 1, 1, 1])

    def test_(self):
        
        self.assertTrue(ex_18_sol.MisterRobot(4, [0, 0, 0, 0])) # test 1
        self.assertTrue(ex_18_sol.MisterRobot(4, [3, 2, 4, 1])) # test 2
        self.assertTrue(ex_18_sol.MisterRobot(7, [1, 3, 4, 5, 6, 2, 7])) # test 3
        self.assertFalse(ex_18_sol.MisterRobot(4, [2, 4, 1, 3])) # test 4

if __name__ == "__main__":
    unittest.main()
