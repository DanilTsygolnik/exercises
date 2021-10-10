import unittest
import ex_21_sol

def fact(N):
    
    def iter(product, count, N):
        if count > N:
            return product
        else:
            return iter(product*count, count+1, N)

    return iter(1, 1, N)

class Test_ex_21_sol(unittest.TestCase):

    def test_fact(self):
        
        self.assertEqual(fact(0), 1)
        self.assertEqual(fact(1), 1)
        self.assertEqual(fact(2), 2)
        self.assertEqual(fact(3), 6)
        self.assertEqual(fact(4), 24)

    def test_switch_letters(self):
        
        self.assertEqual(ex_21_sol.switch_letters('abcd', 1), 'bacd')
        self.assertEqual(ex_21_sol.switch_letters('abcd', 2), 'cbad')
        self.assertEqual(ex_21_sol.switch_letters('abcd', 3), 'dbca')

    def test_get_combos(self):
        
        combos = ex_21_sol.get_combos('123')
        ref = ['123', '213', '231', '132', '312', '321']
        for i in ref:
            self.assertTrue(i in combos)

        self.assertEqual(len(ex_21_sol.get_combos('123')), fact(3))
        self.assertEqual(len(ex_21_sol.get_combos('1234')), fact(4))
        self.assertEqual(len(ex_21_sol.get_combos('12345')), fact(5))

        # next: проверить работу на комбинациях с повторяющимися эл-тами


    #def test_func(self):
    #    
    #    self.assertEqual(ex_21_sol.func(), )


if __name__ == "__main__":
    unittest.main()
