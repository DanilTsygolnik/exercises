import unittest
import ex_18_sol

class Test_ex_18_sol(unittest.TestCase):

    def test_is_sort(self):
        
        self.assertTrue(ex_18_sol.is_sort([0, 0, 0, 0]))
        self.assertTrue(ex_18_sol.is_sort([1, 2, 2, 3]))
        self.assertTrue(ex_18_sol.is_sort([1, 2, 3, 4]))

    def test_get_rotated_src(self):
        
        test_list = [1, 1, 1, 2, 3, 4, 1, 1, 1]
        ex_18_sol.get_rotated_src(test_list, 3)
        self.assertEqual(test_list, [1, 1, 1, 3, 4, 2, 1, 1, 1])
        ex_18_sol.get_rotated_src(test_list, 3)
        self.assertEqual(test_list, [1, 1, 1, 4, 2, 3, 1, 1, 1])
        ex_18_sol.get_rotated_src(test_list, 3)
        self.assertEqual(test_list, [1, 1, 1, 2, 3, 4, 1, 1, 1])
        

    def test_(self):
        
        self.assertTrue(ex_18_sol.MisterRobot(4, [0, 0, 0, 0])) # test 1.0
        self.assertTrue(ex_18_sol.MisterRobot(4, [1, 1, 1, 1])) # test 1.1
        self.assertTrue(ex_18_sol.MisterRobot(4, [1, 2, 3, 4])) # test 1.2
        self.assertTrue(ex_18_sol.MisterRobot(4, [3, 2, 4, 1])) # test 1.3
        self.assertTrue(ex_18_sol.MisterRobot(5, [1, 2, 3, 4, 5])) # test 2.1
        self.assertTrue(ex_18_sol.MisterRobot(5, [1, 2, 4, 5, 3])) # test 2.2
        self.assertTrue(ex_18_sol.MisterRobot(5, [1, 3, 4, 5, 6])) # test 2.3
        self.assertTrue(ex_18_sol.MisterRobot(5, [1, 3, 6, 2, 7])) # test 2.4

        self.assertFalse(ex_18_sol.MisterRobot(4, [2, 4, 1, 3])) # test 3.1
        self.assertFalse(ex_18_sol.MisterRobot(6, [1, 3, 4, 6, 2, 7])) # test 3.2

        self.assertTrue(ex_18_sol.MisterRobot(7, [1, 3, 4, 5, 6, 2, 7])) # test 4 (suggested)

if __name__ == "__main__":
    unittest.main()
