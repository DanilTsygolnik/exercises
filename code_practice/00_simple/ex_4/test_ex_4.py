import unittest
import random
import draft
import ex_4_sol

class TestEx_4(unittest.TestCase):

    def test_MadMax(self):
        for N in range(1, 13, 2):
            Tele = []
            cnt = 0
            while cnt < N:
                Tele.append(random.randint(0,255))
                cnt += 1
            self.assertEqual(ex_4_sol.MadMax(N, Tele), draft.MadMax(N, Tele))

if __name__ == "__main__":
    unittest.main()
