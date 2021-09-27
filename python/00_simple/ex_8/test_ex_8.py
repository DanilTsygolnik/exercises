import unittest
import random
import ex_8_sol

class TestEx_8_sol(unittest.TestCase):

    def test_SumOfThe(self):

        self.assertEqual(ex_8_sol.SumOfThe(7, [100, -50, 10, -25, 90, -35, 90]), 90)
        self.assertEqual(ex_8_sol.SumOfThe(5, [5, -25, 10, -35, -45]), -45)

        for N in [2, 3, 5, 6]:
            data = []
            sum_curr = 0
            cnt = 0
            while cnt < N:
                if cnt == N - 1:
                    data += [sum_curr]
                else:
                    curr = random.randint(-100, 100)
                    sum_curr += curr
                    data += [curr]
                cnt += 1
            check_value = data[N-1]
            random.shuffle(data)

            self.assertEqual(ex_8_sol.SumOfThe(N, data), check_value)

if __name__ == "__main__":
    unittest.main()
