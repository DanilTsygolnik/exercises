import unittest
import ex_25_sol

class Test_ex_25_sol(unittest.TestCase):

    def test_TransformTransform(self):
    
        self.assertTrue(ex_25_sol.TransformTransform([1,2,3,4], 4))
        self.assertFalse(ex_25_sol.TransformTransform([1,2,3,5], 4))


if __name__ == "__main__":
    unittest.main()
