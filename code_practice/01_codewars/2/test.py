import unittest
from sol import get_combos
from sol import brackets

class Test(unittest.TestCase):

    def test_(self):
        ref = ['aa', 'ab', 'ba', 'bb']
        result = []
        for i in get_combos(2, ['a', 'b']).values():
            result.append("".join(i))
        self.assertEqual(result, ref)

    def test_(self):
        """
        Бесконечный цикл при k=0
        Нужно обязательно добавить проверку на предмет:
        - values=[] -- <type list>
        - i for i in values: type(i)==type('string')
        """
        ref = []
        for k in range(1,5):
            result = []
            for i in get_combos(k, ['a', 'b', 'c']).values():
                result.append("".join(i))
            print(f"{result} -- {len(result)}")
        #self.assertEqual(result, ref)

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
