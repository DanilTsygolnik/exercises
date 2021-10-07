import unittest
import ex_19_sol

class Test_ex_19_sol(unittest.TestCase):

    def test_chains(self):
        
        self.assertEqual(ex_19_sol.chains([1, 1, 1, 1]), [[0, 3]])
        self.assertEqual(ex_19_sol.chains([4, 4, 4, 4, 5, 6, 7]), [[0, 3]])
        self.assertEqual(ex_19_sol.chains([1, 2, 3, 4, 4, 4, 4, 5, 6, 7]), [[3, 6]])
        self.assertEqual(ex_19_sol.chains([1, 2, 3, 4, 4, 4, 4]), [[3, 6]])
        self.assertEqual(ex_19_sol.chains([1, 2, 3, 4, 4, 4, 4, 5, 6, 7, 8, 8, 8, 8, 9, 10]), [[3, 6], [10, 13]])
        self.assertEqual(ex_19_sol.chains([1, 2, 3, 4, 4, 4, 4, 5, 6, 7, 8, 8, 8, 8]), [[3, 6], [10, 13]])
        self.assertEqual(ex_19_sol.chains([4, 4, 4, 4, 5, 6, 7, 8, 8, 8, 8]), [[0, 3], [7, 10]])

    def test_get_data_templ(self):

        inp_list = ['платье1 5', 'сумка32 2', 'платье1 1', 'сумка23 2', 'сумка128 4']
        self.assertEqual(ex_19_sol.get_data_templ(inp_list), [['платье1', 6], ['сумка32', 2], ['сумка23', 2], ['сумка128', 4]])

    def test_ShopOLAP(self):
        
        inp_list = ['платье1 5', 'сумка32 2', 'платье1 1', 'сумка23 2', 'сумка128 4']
        self.assertEqual(ex_19_sol.ShopOLAP(5, inp_list), [['платье1', 6], ['сумка128', 4], ['сумка23', 2], ['сумка32', 2]])


if __name__ == "__main__":
    unittest.main()
