import unittest
import ex_9_sol

class Test_ex_9_sol(unittest.TestCase):

    def test_TheRabbitsFoot(self):

            self.assertEqual(ex_9_sol.TheRabbitsFoot('отдай мою кроличью лапку'), 'омоюу толл дюиа акчп йрьк')
            self.assertEqual(ex_9_sol.TheRabbitsFoot('омоюу толл дюиа акчп йрьк', False), 'отдаймоюкроличьюлапку')

if __name__ == "__main__":
    unittest.main()
