import unittest
import ex_28_sol

class Test_ex_28_sol(unittest.TestCase):

    def test_Keymaker(self):
        
        for i in range(0,100):
            self.assertEqual(ex_28_sol.Keymaker(i), ex_28_sol.Keymaker_math(i))


if __name__ == "__main__":
    unittest.main()
