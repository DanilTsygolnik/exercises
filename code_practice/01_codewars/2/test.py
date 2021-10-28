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
        test_cases = (
                        # [args, answer]
                        [['2', '1', '2'], 6], 
                        [['2', '1', '1'], 4], 
                        [['2', '2', '4'], 16], 
                        [['3', '3', '3'], 27], 
                        [['1', '1', '1'], 3], 
                        [['1', '2', '3'], 9], 
                        [['1', '3', '1'], 5], 
                        [['2', '2', '2'], 8], 
                        [['5', '1', '3'], 20], 
                        [['3', '5', '7'], 105], 
                        [['5', '6', '1'], 35], 
                        [['1', '6', '1'], 8], 
                        [['2', '6', '1'], 14], 
                        [['6', '7', '1'], 48], 
                        [['1', '8', '3'], 27], 
                        [['9', '7', '2'], 126], 
                        [['9', '1', '1'], 18], 
                        [['1', '10', '1'], 12], 
                        [['2', '10', '3'], 60], 
                        [['1', '1', '10'], 20], 
                        [['10', '5', '6'], 300] 
                     )
        for i in test_cases:
            args = i[0]
            ref = i[1]
            signs = ['+', '*']
            sig_combos = get_combos(len(args)-1, signs)
            self.assertEqual(max_expr_val(args, sig_combos), ref)
    

if __name__=="__main__":
    unittest.main()
