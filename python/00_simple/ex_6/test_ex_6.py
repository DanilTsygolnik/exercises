import unittest
import ex_6_sol

class TestEx_6_sol(unittest.TestCase):

    def test_PatternUnlock(self):
        self.assertEqual(ex_6_sol.PatternUnlock(0, []), "")
        self.assertEqual(ex_6_sol.PatternUnlock(2, [5, 6]), "1")
        self.assertEqual(ex_6_sol.PatternUnlock(2, [2, 6]), "141421")
        self.assertEqual(ex_6_sol.PatternUnlock(5, [7, 8, 2, 1, 5]), "441421")
        self.assertEqual(ex_6_sol.PatternUnlock(6, [9, 1, 9, 8, 2, 7]), "541421")
        self.assertEqual(ex_6_sol.PatternUnlock(10, [1, 2, 3, 4, 5, 6, 2, 7, 8, 9]), "982843")

if __name__ == "__main__":
    unittest.main()
