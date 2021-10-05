import unittest
import ex_16_sol

class Test_ex_16_sol(unittest.TestCase):

    def test_MaximumDiscount(self):
        
        # suggested tests
        self.assertEqual(ex_16_sol.MaximumDiscount(3, [400, 300, 250]), 250)
        self.assertEqual(ex_16_sol.MaximumDiscount(7, [400, 350, 300, 250, 200, 150, 100]), 450)

        self.assertEqual(ex_16_sol.MaximumDiscount(0, []), 0)
        self.assertEqual(ex_16_sol.MaximumDiscount(1, [400]), 0)
        self.assertEqual(ex_16_sol.MaximumDiscount(2, [400, 500]), 0)

if __name__ == "__main__":
    unittest.main()
