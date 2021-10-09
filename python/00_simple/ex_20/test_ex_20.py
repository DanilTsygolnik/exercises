import unittest
import ex_20_sol

class Test_ex_20_sol(unittest.TestCase):

    def test_S_is_number(self):
        
        self.assertTrue(ex_20_sol.S_is_number('5'))
        self.assertFalse(ex_20_sol.S_is_number('xx'))

    #def test_func(self):
    #    
    #    self.assertEqual(ex_20_sol.func(), )

if __name__ == "__main__":
    unittest.main()
