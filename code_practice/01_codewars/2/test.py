import unittest
from sol import get_combos
from sol import brackets

class Test(unittest.TestCase):

    def test_get_combos(self):
        cases = ((1, ['1', 2]), (0, 'abcd'))
        for i in cases:
            with self.assertRaises(AssertionError):
                get_combos(*i)

        self.assertEqual(get_combos(0, ['a', 'b']), [])
        ref = [['a'], ['b']]
        self.assertEqual(get_combos(1, ['a', 'b']), ref)
        ref = [['a', 'a'], ['a', 'b'], ['b', 'a'], ['b', 'b']]
        self.assertEqual(get_combos(2, ['a', 'b']), ref)

    def test_brackets(self):
        """
        в функцию get_combos добавить exception:
        - на вход должно поступать не менее двух эл-тов для будущего выражения

        здесь
        м.б. стоит поправить вывод для списка из одно эл-та
        """
        print(brackets([]))
        print(brackets(['1']))
        print(brackets(['1','2']))
        print(brackets(['1','2','3']))
        print(brackets(['1','2','3','4']))
        print(brackets(['1','2','3','4', '5']))

if __name__=="__main__":
    unittest.main()
