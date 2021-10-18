import unittest
import ex_27_sol

def factorial(number):
    def iter(prod, cnt, number):
        if cnt > number:
            return prod
        return iter(prod*cnt, cnt+1, number)

    return iter(1, 1, number)

class Test_ex_27_sol(unittest.TestCase):

    def test_str_from_list(self):
        
        self.assertEqual(ex_27_sol.str_from_list([]), "")
        self.assertEqual(ex_27_sol.str_from_list(['q']), "q")
        self.assertEqual(ex_27_sol.str_from_list(['a', 'bcd']), "abcd")
        self.assertEqual(ex_27_sol.str_from_list([1]), "1")
        self.assertEqual(ex_27_sol.str_from_list([1,2,3,4]), "1234")

    def test_get_combos_rule_one(self):
        
        ref = {"":[]} # test 0
        self.assertEqual(ex_27_sol.get_combos_rule_one([]), ref.keys())
        
        ref = {"1":[1]} # test 1
        self.assertEqual(ex_27_sol.get_combos_rule_one([1]), ref.keys())
        
        ref = {"12":[1,2], "21":[2,1]} # test 3
        self.assertEqual(ex_27_sol.get_combos_rule_one([1,2]), ref.keys())

        ref = {"123":[1,2,3], "213":[2,1,3], "132":[1,3,2], "321":[3,2,1]} # test 4
        self.assertEqual(ex_27_sol.get_combos_rule_one([1,2,3]), ref.keys())

    #def test_func(self):
    #    
    #    self.assertEqual(ex_27_sol.func(), )


if __name__ == "__main__":
    unittest.main()
