import unittest
import ex_11_sol

class Test_ex_11_sol(unittest.TestCase):

    def test_big_num_small_num(self):
        
        self.assertEqual(ex_11_sol.big_num_small_num('111', '1111'), ['1111', '111'])
        self.assertEqual(ex_11_sol.big_num_small_num('2222', '222'), ['2222', '222'])
        self.assertEqual(ex_11_sol.big_num_small_num('2222', '2223'), ['2223', '2222'])
        self.assertEqual(ex_11_sol.big_num_small_num('2442', '2223'), ['2442', '2223'])

    def test_add_zeros(self):
        
        self.assertEqual(ex_11_sol.add_zeros('222222', '222'), '000222')
        self.assertEqual(ex_11_sol.add_zeros('222', '222'), '222')

    def test_BigMinus(self):
        
        self.assertEqual(ex_11_sol.BigMinus('54321', '12345'), '41976')
        self.assertEqual(ex_11_sol.BigMinus('54321', ''), '54321')
        self.assertEqual(ex_11_sol.BigMinus('', '54321'), '54321')
        self.assertEqual(ex_11_sol.BigMinus('11111', '111'), '11000')
        self.assertEqual(ex_11_sol.BigMinus('10000', '1'), '9999')
        self.assertEqual(ex_11_sol.BigMinus(str(10**16), '1'), str(10**16 - 1))
        self.assertEqual(ex_11_sol.BigMinus(str(10**16), str(10**16)), '0')
        self.assertEqual(ex_11_sol.BigMinus('1', '5'), '4')
        self.assertEqual(ex_11_sol.BigMinus('000', '00'), '0')
        self.assertEqual(ex_11_sol.BigMinus('000', ''), '0')
        self.assertEqual(ex_11_sol.BigMinus('', '00'), '0')
        self.assertEqual(ex_11_sol.BigMinus('1', '1'), '0')
        self.assertEqual(ex_11_sol.BigMinus('', ''), '')

if __name__ == "__main__":
    unittest.main()
