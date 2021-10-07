import unittest
import ex_19_sol

class Test_ex_19_sol(unittest.TestCase):

    def test_get_data_templ(self):

        inp_list = ['платье1 5', 'сумка32 2', 'платье1 1', 'сумка23 2', 'сумка128 4']
        self.assertEqual(ex_19_sol.get_data_templ(inp_list), [['платье1', 6], ['сумка32', 2], ['сумка23', 2], ['сумка128', 4]])

    def test_ShopOLAP(self):
        
        # suggested test
        inp_list = ['платье1 5', 
                    'сумка32 2', 
                    'платье1 1', 
                    'сумка23 2', 
                    'сумка128 4']
        
        self.assertEqual(ex_19_sol.ShopOLAP(5, inp_list), [['платье1', 6], ['сумка128', 4], ['сумка23', 2], ['сумка32', 2]])

        # test 1
        inp_list = ['платье1 5']
        
        self.assertEqual(ex_19_sol.ShopOLAP(5, inp_list), [['платье1', 5]])

        # test 2
        inp_list = ['сумка32 2', 
                    'сумка23 2', 
                    'сумка128 4']
        
        self.assertEqual(ex_19_sol.ShopOLAP(5, inp_list), [['сумка128', 4], ['сумка23', 2], ['сумка32', 2]])

        # test 3
        inp_list = ['сумка32 2', 
                    'сумка23 2', 
                    'сумка128 2']
        
        self.assertEqual(ex_19_sol.ShopOLAP(5, inp_list), [['сумка23', 2], ['сумка32', 2], ['сумка128', 2]])



if __name__ == "__main__":
    unittest.main()
