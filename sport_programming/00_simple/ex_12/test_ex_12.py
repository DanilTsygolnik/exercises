import unittest
import ex_12_sol

class Test_ex_12_sol(unittest.TestCase):

    def test_MassVote(self):
        
        self.assertEqual(ex_12_sol.MassVote(5, [10, 10, 15, 5, 60]), 'majority winner 5')
        self.assertEqual(ex_12_sol.MassVote(5, [60, 10, 10, 15, 5]), 'majority winner 1')
        self.assertEqual(ex_12_sol.MassVote(3, [10, 15, 10]), 'minority winner 2')
        self.assertEqual(ex_12_sol.MassVote(4, [111, 111, 110, 110]), 'no winner')
        self.assertEqual(ex_12_sol.MassVote(7, [111, 111, 55, 110, 110, 55, 90]), 'no winner')
        self.assertEqual(ex_12_sol.MassVote(1, [100500]), 'majority winner 1')


if __name__ == "__main__":
    unittest.main()
