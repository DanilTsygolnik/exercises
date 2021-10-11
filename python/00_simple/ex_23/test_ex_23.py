import unittest
import ex_23_sol

class Test_ex_23_sol(unittest.TestCase):

    def test_get_data(self):
        
        str_input = ['']
        ref = [[]]

        self.assertEqual(ex_23_sol.get_data(str_input), ref)

        str_input = [
                        '.+..', 
                        '..+.', 
                        '.+..']
        ref = [
                [[0,'.'], [1,'+'], [0,'.'], [0,'.']], 
                [[0,'.'], [0,'.'], [1,'+'], [0,'.']], 
                [[0,'.'], [1,'+'], [0,'.'], [0,'.']]]

        self.assertEqual(ex_23_sol.get_data(str_input), ref)

        str_input = ['.+..']

        ref = [[[0,'.'], [1,'+'], [0,'.'], [0,'.']]]

        self.assertEqual(ex_23_sol.get_data(str_input), ref)

    def test_aging(self):
        
        inp = [
                [[0,'.'], [1,'+'], [0,'.'], [0,'.']], 
                [[0,'.'], [0,'.'], [1,'+'], [0,'.']], 
                [[1,'+'], [2,'+'], [0,'.'], [0,'.']]]

        ref = [
                [[1,'+'], [2,'+'], [1,'+'], [1,'+']], 
                [[1,'+'], [1,'+'], [2,'+'], [1,'+']], 
                [[2,'+'], [3,'+'], [1,'+'], [1,'+']]]

        self.assertEqual(ex_23_sol.aging(inp), ref)

    def test_decay(self):
        
        inp = [
                [[2,'+'], [2,'+'], [2,'+'], [4,'+']], 
                [[4,'+'], [2,'+'], [2,'+'], [2,'+']], 
                [[2,'+'], [2,'+'], [2,'+'], [4,'+']]]

        ref = [
                [[0,'.'], [2,'+'], [0,'.'], [0,'.']], 
                [[0,'.'], [0,'.'], [2,'+'], [0,'.']], 
                [[0,'.'], [2,'+'], [0,'.'], [0,'.']]]

        self.assertEqual(ex_23_sol.decay(inp, 3, 4), ref)

    def test_TreeOfLife(self):
        
        # suggested 
        self.assertEqual(ex_23_sol.TreeOfLife(3, 4, 4, [".+..","..+.",".+.."]), [".+..","..+.",".+.."])
        # extra
        self.assertEqual(ex_23_sol.TreeOfLife(3, 4, 12, [".+..","..+.",".+.."]), [".+..","..+.",".+.."])
        self.assertEqual(ex_23_sol.TreeOfLife(3, 4, 8, [".+..","..+.",".+.."]), [".+..","..+.",".+.."])
        self.assertEqual(ex_23_sol.TreeOfLife(3, 4, 7, [".+..","..+.",".+.."]), ["++++","++++","++++"])
        self.assertEqual(ex_23_sol.TreeOfLife(3, 4, 3, [".+..","..+.",".+.."]), ["++++","++++","++++"])
        self.assertEqual(ex_23_sol.TreeOfLife(3, 4, 11, [".+..","..+.",".+.."]), ["++++","++++","++++"])
        self.assertEqual(ex_23_sol.TreeOfLife(3, 4, 2, ["++++","++++","++++"]), ["....","....","...."])
        self.assertEqual(ex_23_sol.TreeOfLife(3, 4, 3, ["++++","++++","++++"]), ["++++","++++","++++"])
        self.assertEqual(ex_23_sol.TreeOfLife(3, 4, 4, ["....","....","...."]), ["....","....","...."])
        self.assertEqual(ex_23_sol.TreeOfLife(3, 4, 5, ["....","....","...."]), ["++++","++++","++++"])

        # problem
        self.assertEqual(ex_23_sol.TreeOfLife(6,7,24,['.......','...+...','....+..','.......','++.....','++.....']), ['.......','...+...','....+..','.......','++.....','++.....'])


if __name__ == "__main__":
    unittest.main()
