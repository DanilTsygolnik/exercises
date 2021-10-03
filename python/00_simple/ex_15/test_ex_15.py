import unittest
import ex_15_sol

class Test_ex_15_sol(unittest.TestCase):

    def test_get_strings(self):
        
        self.assertEqual(ex_15_sol.get_strings(''), [])
        self.assertEqual(ex_15_sol.get_strings(' '), [])
        self.assertEqual(ex_15_sol.get_strings('   '), [])
        self.assertEqual(ex_15_sol.get_strings('1234'), ['1234'])
        self.assertEqual(ex_15_sol.get_strings('1234 '), ['1234'])
        self.assertEqual(ex_15_sol.get_strings('1234 2345 0987'), ['1234', '2345', '0987'])
        self.assertEqual(ex_15_sol.get_strings('1234 2345 0987 '), ['1234', '2345', '0987'])

    def test_find_all(self):
        
        string = '111112211112211221111122'
        self.assertEqual(ex_15_sol.find_all(string, '22'), [5, 11, 15, 22])

    def test_get_search_res(self):

        # case 1
        strings = ex_15_sol.get_strings('2211111111 1111111122 2211111122 1122111221')
        #    ----------
        #    2211111111
        #    1111111122
        #    2211111122
        #    1122111221
        #    ----------
        words = ex_15_sol.get_strings('22')
        case_1_ref = [[[0, 0, 0], [0, 1, 8], [0, 2, 0], [0, 2, 8], [0, 3, 2], [0, 3, 7]]]

        self.assertEqual(ex_15_sol.get_search_res(strings, words), case_1_ref)

        # case 2
        strings = ex_15_sol.get_strings('2211111133 3311111122 2213313322 1122133221')
        #    ----------
        #  0 2211111133
        #  1 3311111122 -- первая строка, в которой ищем 33
        #  2 2213313322 -- последняя строка, в которой ищем 22
        #  3 1122133221 -- последняя строка, в которой ищем 33; 22 уже не ищем
        #    ----------
        words = ex_15_sol.get_strings('22 33')
        case_2_ref = [
                        [[0, 0, 0], [0, 1, 8], [0, 2, 0], [0, 2, 8]], 
                        [[1, 1, 0], [1, 2, 3], [1, 2, 6], [1, 3, 5]]
        ]

        self.assertEqual(ex_15_sol.get_search_res(strings, words), case_2_ref)

        # suggested test case
        strings = ex_15_sol.get_strings('1234 2345 0987')
        #  j ---------- i----
        #  0 1234       0 34 - поиск в j = 0,1
        #  1 2345       1 98  - поиск в j = 1,2
        #  2 0987         
        #    ---------- -----
        words = ex_15_sol.get_strings('34 98')
        case_ref = [
                        [[0, 0, 2], [0, 1, 1]], 
                        [[1, 2, 1]]
        ]

        self.assertEqual(ex_15_sol.get_search_res(strings, words), case_ref)

    def test_TankRush(self):
        
        self.assertEqual(ex_15_sol.TankRush(3, 4, '1234 2345 0987', 2, 2, '34 90'), False) # 1
        self.assertEqual(ex_15_sol.TankRush(3, 4, '1234 2345 0987', 2, 2, '34 98'), True) # 2
        self.assertEqual(ex_15_sol.TankRush(3, 4, '1234 2345 0987', 2, 2, '34 45'), True) # 3
        self.assertEqual(ex_15_sol.TankRush(3, 4, '1234 2345 0987', 2, 2, '345 987'), True) # 4
        self.assertEqual(ex_15_sol.TankRush(3, 4, '1234 2345 0987', 2, 2, '2345 0987'), True) # 5
        self.assertEqual(ex_15_sol.TankRush(3, 4, '1234 2345 0987', 2, 2, '5 7'), True) # 6
        self.assertEqual(ex_15_sol.TankRush(1, 1, '1 1', 1, 1, '1 1'), True) # 7
        self.assertEqual(ex_15_sol.TankRush(1, 1, '1 1', 0, 0, ''), False) # 8
        self.assertEqual(ex_15_sol.TankRush(0, 0, '', 1, 1, '1 1'), False) # 9
        self.assertEqual(ex_15_sol.TankRush(0, 0, '', 0, 0, ''), True) # 10

        #   k 0123     01
        #  j  ----   i --------
        #  0  1331   0 22 -- s_res(i=0): [[2, 1]]
        #  1  1111   1 33 -- s_res(i=1): [[0, 1], [3, 1]]
        #  2  1221             
        #  3  1331             
        #  4  1111             
        #     ----     --------

        self.assertEqual(ex_15_sol.TankRush(5, 4, '1331 1111 1221 1331 1111', 2, 2, '22 33'), True) # 11

        #   k 0123     01
        #  j  ----   i --------
        #  0  1331   0 22 -- s_res(i=0): [[2, 1]]
        #  1  1111   1 33 -- s_res(i=1): [[0, 1]]
        #  2  1221             
        #  3  1111             
        #  4  1111             
        #     ----     --------

        self.assertEqual(ex_15_sol.TankRush(5, 4, '1331 1111 1221 1111 1111', 2, 2, '22 33'), False) # 12

if __name__ == "__main__":
    unittest.main()
