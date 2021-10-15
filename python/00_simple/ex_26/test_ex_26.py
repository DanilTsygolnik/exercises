import unittest
import ex_26_sol

class Test_ex_26_sol(unittest.TestCase):

    def test_get_pairs(self):
        
        #  0123456789
        # "5==ooooooo" --> []
        # "abc=7==hdj" --> []
        # "axxb6===4x" --> [[5,8]]
        # "9===1===9=" --> [[1,4], [5,8]]

        self.assertEqual(ex_26_sol.get_pairs("5==ooooooo"), [])
        self.assertEqual(ex_26_sol.get_pairs("abc=7==hdj"), [])
        self.assertEqual(ex_26_sol.get_pairs("axxb6===4x"), [[5,8]])
        self.assertEqual(ex_26_sol.get_pairs("9===1===9="), [[1,4], [5,8]])

    #def test_func(self):
    #    
    #    self.assertEqual(ex_26_sol.func(), )


if __name__ == "__main__":
    unittest.main()
