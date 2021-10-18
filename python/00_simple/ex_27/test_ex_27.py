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

    #def test_func(self):
    #    
    #    self.assertEqual(ex_27_sol.func(), )


if __name__ == "__main__":
    unittest.main()
