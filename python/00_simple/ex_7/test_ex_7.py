import unittest
import ex_7_sol

class TestEx_7_sol(unittest.TestCase):

    def test_WordSearch(self):
        self.assertEqual(
        ex_7_sol.WordSearch(3, "1) строка разбивается на набор строк через выравнивание по заданной ширине", "зад"), 
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0])

        self.assertEqual(
        ex_7_sol.WordSearch(12, "1) строка разбивается на набор строк через выравнивание по заданной ширине", "строк"), 
        [0, 0, 0, 1, 0, 0, 0])


if __name__ == "__main__":
    unittest.main()
