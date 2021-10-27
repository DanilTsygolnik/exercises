import unittest
import ex_17_sol

class Test_ex_17_sol(unittest.TestCase):

    def test_LineAnalysis(self):
        
        self.assertTrue(ex_17_sol.LineAnalysis('*'))
        self.assertTrue(ex_17_sol.LineAnalysis('***'))
        self.assertTrue(ex_17_sol.LineAnalysis('**'))
        self.assertTrue(ex_17_sol.LineAnalysis('*.*'))
        self.assertTrue(ex_17_sol.LineAnalysis('*.......*'))
        self.assertTrue(ex_17_sol.LineAnalysis('*.......*.......*'))
        self.assertTrue(ex_17_sol.LineAnalysis('*..*..*..*..*..*..*'))

        self.assertFalse(ex_17_sol.LineAnalysis('*..*...*..*..*..*..*'))
        self.assertFalse(ex_17_sol.LineAnalysis('*..*..*..*..*..**..*'))
        self.assertFalse(ex_17_sol.LineAnalysis('*.......*..'))

if __name__ == "__main__":
    unittest.main()
