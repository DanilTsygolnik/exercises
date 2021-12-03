import unittest
from random import randint
from is_palindrome import is_palindrome

class TestFunc(unittest.TestCase):
 
    def test_main(self):
        self.assertTrue(is_palindrome(""))
        self.assertTrue(is_palindrome("a"))
        self.assertTrue(is_palindrome("aa"))
        self.assertTrue(is_palindrome("aba"))
        self.assertTrue(is_palindrome("abba"))
        self.assertTrue(is_palindrome("abcba"))
        self.assertFalse(is_palindrome("ab"))
        self.assertFalse(is_palindrome("abb"))
        self.assertFalse(is_palindrome("abbb"))
        self.assertFalse(is_palindrome("abcaa"))

if __name__=="__main__":
    unittest.main()
