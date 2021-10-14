import unittest
import ex_24_sol

class Test_ex_24_sol(unittest.TestCase):

    def test_prepare_matrix(self):
        
        ref = [['1', '2', '3', '4', '5', '6'], 
               ['2', '3', '4', '5', '6', '7'], 
               ['3', '4', '5', '6', '7', '8'], 
               ['4', '5', '6', '7', '8', '9']]
        self.assertEqual(ex_24_sol.prepare_matrix(["123456", "234567", "345678", "456789"]), ref)

    #def test_func(self):
    #    
    #    self.assertEqual(ex_24_sol.func(), )


if __name__ == "__main__":
    unittest.main()
