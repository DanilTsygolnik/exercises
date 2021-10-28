import unittest
from sol import get_combos
from sol import max_expr_val

class Test(unittest.TestCase):

    def test_get_combos(self):
        """
        в функцию get_combos добавить exception:
        - на вход должно поступать не менее двух эл-тов для будущего выражения
        """
        cases = ((1, ['1', 2]), (0, 'abcd'))
        for i in cases:
            with self.assertRaises(AssertionError):
                get_combos(*i)

        self.assertEqual(get_combos(0, ['a', 'b']), [])
        ref = [['a'], ['b']]
        self.assertEqual(get_combos(1, ['a', 'b']), ref)
        ref = [['a', 'a'], ['a', 'b'], ['b', 'a'], ['b', 'b']]
        self.assertEqual(get_combos(2, ['a', 'b']), ref)

class TestMaxExprVal(unittest.TestCase):

    def test_input_assertions(self):
        """
        test_max_expr_val(args, sig_combos)
        ---
        args=[]; each argument must be str()
        sig_combos=[]; acquire with get_combos(len(args)-1, ['+','*'])
        """

        cases = (
                    ('str', []), # args is not []
                    ([1,2], []), # elements in args are not str() type
                    (['1','2','3'], 'abcd') # sig_combos is not []
                )
        for i in cases:
            with self.assertRaises(AssertionError):
                max_expr_val(*i)

    def test_output(self):
        args = ['1','2','3']
        signs = ['+', '*']
        sig_combos = get_combos(len(args)-1, signs)
        print(max_expr_val(args, sig_combos))
    

if __name__=="__main__":
    unittest.main()
