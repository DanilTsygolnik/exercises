import unittest
from valid_parentheses import valid_parentheses

class TestFunc(unittest.TestCase):
    
    def test_main(self):
        test_samples = \
        [
            ("test 0", "", True),
            ("test 1", "(", False),
            ("test 2", ")", False),
            ("test 3", "   (", False),
            ("test 4", "   )", False),
            ("test 5", ")(", False),
            ("test 6", "(()", False),
            ("test 7", "((()", False),
            ("test 8", "()", True),
            ("test 9", "(())", True),
            ("test 10", "()()", True),
            ("test 11", ")())", False),
            ("test 12", "((()", False),
            ("test 13", "((()))", True),
            ("test 14", "(()())", True),
            ("test 15", "())(()", False),
            ("test 16", ")()()(", False),
            ("test 17", "(((())))", True),
            ("test 18", "((()()))", True),
            ("test 19", "(())(())", True),
            ("test 20", "((()))))", False),
            ("test 21", "()))((()", False)
        ]
        for i in test_samples:
            print(i[0])
            self.assertIs(valid_parentheses(i[1]), i[2])

if __name__ == "__main__":
    unittest.main()
