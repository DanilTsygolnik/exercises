import unittest
import ex_24_sol

class Test_ex_24_sol(unittest.TestCase):

    def test_prepare_matrix(self):
        
        ref = [['1', '2', '3', '4', '5', '6'], 
               ['2', '3', '4', '5', '6', '7'], 
               ['3', '4', '5', '6', '7', '8'], 
               ['4', '5', '6', '7', '8', '9']]
        self.assertEqual(ex_24_sol.prepare_matrix(["123456", "234567", "345678", "456789"]), ref)

    def test_get_rings(self):
        
        # solution conditions: (min(N,M) >= 2) and (min(N,M) % 2 == 0)
        # (7,6)
        ref = [[7,6], [5,4], [3,2]]
        self.assertEqual(ex_24_sol.get_rings(7,6), ref)

        # (6,4)
        ref = [[6,4], [4,2]]
        self.assertEqual(ex_24_sol.get_rings(6,4), ref)

        # (6,2)
        ref = [[6,2]]
        self.assertEqual(ex_24_sol.get_rings(6,2), ref)

        # (2,6)
        ref = [[2,6]]
        self.assertEqual(ex_24_sol.get_rings(2,6), ref)

        # (2,2)
        ref = [[2,2]]
        self.assertEqual(ex_24_sol.get_rings(2,2), ref)

    def test_get_cols_as_rows(self):
        
        matrix = [['1', '2', '3', '4'], 
                  ['2', '3', '8', '5'], 
                  ['3', '0', '5', '6'], 
                  ['4', '5', '6', '7']]

        ref = ['2', '3', '4']
        self.assertEqual(ex_24_sol.get_left_col_as_row(4,matrix,0), ref)
        ref = ['0']
        self.assertEqual(ex_24_sol.get_left_col_as_row(4,matrix,1), ref)

        ref = ['4', '5', '6']
        self.assertEqual(ex_24_sol.get_right_col_as_row(4,4,matrix,0), ref)
        ref = ['8']
        self.assertEqual(ex_24_sol.get_right_col_as_row(4,4,matrix,1), ref)

    def test_iter_rotate(self):
        
        matrix = [['1', '2', '3', '4'], 
                  ['2', '3', '8', '5'], 
                  ['3', '0', '5', '6'], 
                  ['4', '5', '6', '7']]

        ref_outer_ring = [['2', '1', '2', '3'], 
                          ['3', '3', '8', '4'], 
                          ['4', '0', '5', '5'], 
                          ['5', '6', '7', '6']]

        ref_inner_ring = [['2', '1', '2', '3'], 
                          ['3', '0', '3', '4'], 
                          ['4', '5', '8', '5'], 
                          ['5', '6', '7', '6']]

        ex_24_sol.iter_rotate(matrix, 4, 4, 0)
        self.assertEqual(matrix, ref_outer_ring)
        ex_24_sol.iter_rotate(matrix, 4, 4, 1)
        self.assertEqual(matrix, ref_inner_ring)

    def test_src_format(self):
        
        matrix = [['1', '2', '3', '4'], 
                  ['2', '3', '8', '5'], 
                  ['3', '0', '5', '6'], 
                  ['4', '5', '6', '7']]

        ref = ['1234', '2385', '3056', '4567']

        self.assertEqual(ex_24_sol.src_format(matrix), ref)

    def test_turn_iter(self):
        
        matrix = [['1', '2', '3', '4'], 
                  ['2', '3', '8', '5'], 
                  ['3', '0', '5', '6'], 
                  ['4', '5', '6', '7']]

        ref = ['2123', '3034', '4585', '5676']

        self.assertEqual(ex_24_sol.turn_iter(matrix, 4, 4), ref)

    def test_MatrixTurn(self):
        
        matrix = ["123456", "234567", "345678", "456789"]
        ref = ['432123', '565434', '676545', '789876']
        ex_24_sol.MatrixTurn(matrix, 4,6, 3)
        self.assertEqual(matrix, ref)

        matrix = ["123456", "234567", "345678", "456789"]
        ref = ["123456", "234567", "345678", "456789"]
        ex_24_sol.MatrixTurn(matrix, 4,6, 0)
        self.assertEqual(matrix, ref)

        matrix = ["123456", "234567", "345678", "456789"]
        ref = ['212345', '343456', '456767', '567898']
        ex_24_sol.MatrixTurn(matrix, 4,6, 1)
        self.assertEqual(matrix, ref)

        matrix = ["123456", "234567", "345678", "456789"]
        ref = ['432123', '565434', '676545', '789876']
        ex_24_sol.MatrixTurn(matrix, 4,6, 3)
        self.assertEqual(matrix, ref)

        matrix = ["12", "34"]
        ref = ['31', '42']
        ex_24_sol.MatrixTurn(matrix, 2,2, 1)
        self.assertEqual(matrix, ref)

        matrix = ["12", "34"]
        ref = ["12", "34"]
        ex_24_sol.MatrixTurn(matrix, 2,2, 4)
        self.assertEqual(matrix, ref)

        matrix = ["123456", "234567", "345678", "456789"]
        ref = ["123456", "234567", "345678", "456789"]
        ex_24_sol.MatrixTurn(matrix, 4,6, 16)
        self.assertEqual(matrix, ref)

        matrix = ["000000", "111111", "000000", "111111", "000000", "111111"]
        ref = ["100000", "001110", "111011", "001000", "100011", "111110"]
        ex_24_sol.MatrixTurn(matrix, 6,6, 1)
        self.assertEqual(matrix, ref)


if __name__ == "__main__":
    unittest.main()
