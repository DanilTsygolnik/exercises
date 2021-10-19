import unittest
import ex_14_sol

class Test_ex_14_sol(unittest.TestCase):

    def test_Unmanned(self):
        
        self.assertEqual(ex_14_sol.Unmanned(10, 2, [[3,5,5], [5,2,2]]), 12)
        self.assertEqual(ex_14_sol.Unmanned(0, 0, []), 0)
        self.assertEqual(ex_14_sol.Unmanned(10, 0, []), 10)
        self.assertEqual(ex_14_sol.Unmanned(10, 2, [[11,5,5],[15,2,2]]), 10)

if __name__ == "__main__":
    unittest.main()
