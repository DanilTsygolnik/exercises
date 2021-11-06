import unittest
import ex_22_sol

class Test_ex_22_sol(unittest.TestCase):

    def test_letters_count(self):
        
        self.assertEqual(ex_22_sol.letters_count('aaa'), [3])
        self.assertEqual(ex_22_sol.letters_count('abc'), [1, 1, 1])
        self.assertEqual(ex_22_sol.letters_count('aaabcdd'), [3, 1, 1, 2])

    def test_SherlockValidString(self):
        
        self.assertTrue(ex_22_sol.SherlockValidString('xyz'))
        self.assertTrue(ex_22_sol.SherlockValidString('xyzaa'))
        self.assertTrue(ex_22_sol.SherlockValidString('xxyyz'))
        self.assertTrue(ex_22_sol.SherlockValidString("xxyyzziii"))
        self.assertTrue(ex_22_sol.SherlockValidString("xyzxyzt"))
        self.assertTrue(ex_22_sol.SherlockValidString("xzzz"))
        self.assertTrue(ex_22_sol.SherlockValidString("xz"))
        self.assertTrue(ex_22_sol.SherlockValidString("xxxxxyyyyyy"))
        self.assertTrue(ex_22_sol.SherlockValidString("xyzxyzttt"))

        self.assertFalse(ex_22_sol.SherlockValidString('xyzzz'))
        self.assertFalse(ex_22_sol.SherlockValidString('xxyyza'))
        self.assertFalse(ex_22_sol.SherlockValidString('xxyyzabc'))
        self.assertFalse(ex_22_sol.SherlockValidString('dddxxyyz'))
        self.assertFalse(ex_22_sol.SherlockValidString("xxyyzzzz"))
        self.assertFalse(ex_22_sol.SherlockValidString("xxyyzzziiioo"))
        self.assertFalse(ex_22_sol.SherlockValidString("xxzzzz"))
        self.assertFalse(ex_22_sol.SherlockValidString("xxxxxyyyyyyy"))
        self.assertFalse(ex_22_sol.SherlockValidString("xyzxyztttt"))

    #def test_func(self):
    #    
    #    self.assertEqual(ex_22_sol.func(), )


if __name__ == "__main__":
    unittest.main()
