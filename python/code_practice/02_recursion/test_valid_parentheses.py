import unittest
from valid_parentheses import valid_parentheses

class TestFunc(unittest.TestCase):
    
    def test_main(self):
        test_samples = \
        [
            ("(", False),
            (")", False),
            ("   (", False),
            ("   )", False),
            (")(", False),
            ("(()", False),
            ("((()", False),
            ("()", True),
            ("(())", True),
            ("()()", True),
        ]
        for i in test_samples:
            self.assertIs(valid_parentheses(i[0]), i[1])

if __name__ == "__main__":
    unittest.main()
