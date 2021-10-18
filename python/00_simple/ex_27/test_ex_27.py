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
        self.assertEqual(ex_27_sol.get_combos_rule_one([]).keys(), ref.keys())
        
        ref = {"1":[1]} # test 1
        self.assertEqual(ex_27_sol.get_combos_rule_one([1]).keys(), ref.keys())
        
        ref = {"12":[1,2], "21":[2,1]} # test 2
        self.assertEqual(ex_27_sol.get_combos_rule_one([1,2]).keys(), ref.keys())

        ref = {"123":[1,2,3], "213":[2,1,3], "132":[1,3,2], "321":[3,2,1]} # test 3
        self.assertEqual(ex_27_sol.get_combos_rule_one([1,2,3]).keys(), ref.keys())

        ref = {'1234':[1,2,3,4], '4231':[4,2,3,1], '3214':[3,2,1,4], '1432':[1,4,3,2], '2134':[2,1,3,4], '1324':[1,3,2,4], '1243':[1,2,4,3]} # test 4
        self.assertEqual(ex_27_sol.get_combos_rule_one([1,2,3,4]).keys(), ref.keys())

    def test_rule_one(self):
        
        self.assertTrue(ex_27_sol.rule_one([1]))
        self.assertTrue(ex_27_sol.rule_one([2,1,3]))
        self.assertTrue(ex_27_sol.rule_one([4,2,3,1]))
        self.assertFalse(ex_27_sol.rule_one([3,1,2]))
        self.assertFalse(ex_27_sol.rule_one([4,3,2,1]))

    #def test_func(self):
    #    
    #    self.assertEqual(ex_27_sol.func(), )


if __name__ == "__main__":
    unittest.main()
