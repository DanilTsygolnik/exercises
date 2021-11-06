import unittest
import ex_19_sol

class Test_ex_19_sol(unittest.TestCase):

<<<<<<< HEAD
    def test_get_data_templ(self):

        inp_list = ['платье1 5']
        self.assertEqual(ex_19_sol.get_data_templ(inp_list), [['платье1', 5]]) 
        inp_list = ['платье1 5', 'сумка32 2', 'платье1 1', 'сумка23 2', 'сумка128 4']
        self.assertEqual(ex_19_sol.get_data_templ(inp_list), [['платье1', 6], 
                                                              ['сумка32', 2], 
                                                              ['сумка23', 2], 
                                                              ['сумка128', 4]])
=======
    def test_get_item_name_and_num(self):

        name = 'платье1'
        self.assertEqual(ex_19_sol.get_item_name_and_num(name), ['платье', 1])
        name = 'платье'
        self.assertEqual(ex_19_sol.get_item_name_and_num(name), ['платье', -1])
        name = 'платье666'
        self.assertEqual(ex_19_sol.get_item_name_and_num(name), ['платье', 666])
        name = ''
        self.assertEqual(ex_19_sol.get_item_name_and_num(name), ['', -1])

    def test_get_data_templ(self):

        inp_list = ['платье1 5']
        self.assertEqual(ex_19_sol.get_data_templ(inp_list), [['платье', 1, 5]]) 
        inp_list = ['платье1 5', 'сумка32 2', 'платье1 1', 'сумка23 2', 'сумка128 4']
        self.assertEqual(ex_19_sol.get_data_templ(inp_list), [['платье', 1, 6], 
                                                              ['сумка', 32, 2], 
                                                              ['сумка', 23, 2], 
                                                              ['сумка', 128, 4]])
>>>>>>> next--ex_20

    def test_chains(self):
        
        self.assertEqual(ex_19_sol.chains([1, 1, 1, 1]), [[0, 3]])
        self.assertEqual(ex_19_sol.chains([1, 2, 2, 1]), [[1, 2]])
        self.assertEqual(ex_19_sol.chains([5, 1, 4, 2, 2]), [[3, 4]])
        self.assertEqual(ex_19_sol.chains([6, 4, 2, 2]), [[2, 3]])
        self.assertEqual(ex_19_sol.chains([4, 4, 4, 4, 5, 6, 7]), [[0, 3]])
        self.assertEqual(ex_19_sol.chains([1, 2, 3, 4, 4, 4, 4, 5, 6, 7]), [[3, 6]])
        self.assertEqual(ex_19_sol.chains([1, 2, 3, 4, 4, 4, 4]), [[3, 6]])
        self.assertEqual(ex_19_sol.chains([1, 2, 3, 4, 4, 4, 4, 5, 6, 7, 8, 8, 8, 8, 9, 10]), [[3, 6], [10, 13]])
        self.assertEqual(ex_19_sol.chains([1, 2, 3, 4, 4, 4, 4, 5, 6, 7, 8, 8, 8, 8]), [[3, 6], [10, 13]])
        self.assertEqual(ex_19_sol.chains([4, 4, 4, 4, 5, 6, 7, 8, 8, 8, 8]), [[0, 3], [7, 10]])

<<<<<<< HEAD
=======

>>>>>>> next--ex_20
    def test_ShopOLAP(self):
        
        # suggested test
        inp_list = ['платье1 5', 
                    'сумка32 2', 
                    'платье1 1', 
                    'сумка23 2', 
<<<<<<< HEAD
=======
                    'бумага 2', 
                    'тетрадь 2', 
>>>>>>> next--ex_20
                    'сумка128 4']
        
        self.assertEqual(ex_19_sol.ShopOLAP(5, inp_list),   ['платье1 6', 
                                                             'сумка128 4', 
<<<<<<< HEAD
                                                             'сумка23 2', 
                                                             'сумка32 2'])

        # suggested_2
        inp_list = ['123 5','32 3','124 5','128 1','32 2','23 4','128 4','128 1']
        self.assertEqual(ex_19_sol.ShopOLAP(8, inp_list), ['128 6','123 5','124 5','32 5','23 4'])

#   # ---------------------------- версия, не прошедшая тест suggested_2 (см. ex_19_sol.py из предыдущего коммита) --------------------
#   def test_ShopOLAP(self):
#       
#       # suggested test
#       inp_list = ['платье1 5', 
#                   'сумка32 2', 
#                   'платье1 1', 
#                   'сумка23 2', 
#                   'бумага 2', 
#                   'тетрадь 2', 
#                   'сумка128 4']
#       
#       self.assertEqual(ex_19_sol.ShopOLAP(5, inp_list),   ['платье1 6', 
#                                                            'сумка128 4', 
#                                                            'бумага 2', 
#                                                            'сумка23 2', 
#                                                            'сумка32 2', 
#                                                            'тетрадь 2'])

#       # test 1
#       inp_list = ['платье1 5']
#       
#       self.assertEqual(ex_19_sol.ShopOLAP(5, inp_list), ['платье1 5'])

#       # test 2
#       inp_list = ['сумка32 2', 
#                   'сумка23 2', 
#                   'сумка128 4']
#       
#       self.assertEqual(ex_19_sol.ShopOLAP(5, inp_list),   [
#                                                            'сумка128 4', 
#                                                            'сумка23 2', 
#                                                            'сумка32 2'])

#       # test 3
#       inp_list = ['сумка32 2', 
#                   'сумка23 2', 
#                   'сумка128 2']
#       
#       self.assertEqual(ex_19_sol.ShopOLAP(5, inp_list),   [
#                                                            'сумка23 2', 
#                                                            'сумка32 2', 
#                                                            'сумка128 2'])

#       # test 4
#       inp_list = ['платье1 5', 
#                   'сумка32 2', 
#                   'платье1 1', 
#                   'сумка23 2', 
#                   'бумага 2', 
#                   'тетрадь 2', 
#                   'сумка128 4', 
#                   'альпака 1',
#                   'альпака2 1',
#                   'арбалет 1',
#                   'амулет1 1',
#                   'амулет2 1']
#       
#       self.assertEqual(ex_19_sol.ShopOLAP(5, inp_list),   ['платье1 6', 
#                                                            'сумка128 4', 
#                                                            'бумага 2', 
#                                                            'сумка23 2', 
#                                                            'сумка32 2', 
#                                                            'тетрадь 2', 
#                                                            'альпака 1', 
#                                                            'альпака2 1', 
#                                                            'амулет1 1', 
#                                                            'амулет2 1', 
#                                                            'арбалет 1'])

#       # test 5
#       inp_list = ['платье1 5', 
#                   'сумка32 2', 
#                   'платье1 1', 
#                   'сумка23 2', 
#                   'бумага 2', 
#                   'тетрадь 2', 
#                   'сумка128 4', 
#                   'альпака 1',
#                   'альпака2 1',
#                   'арбалет 1',
#                   'амулет1 5',
#                   'амулет2 1']
#       
#       self.assertEqual(ex_19_sol.ShopOLAP(5, inp_list),   ['платье1 6', 
#                                                            'амулет1 5', 
#                                                            'сумка128 4', 
#                                                            'бумага 2', 
#                                                            'сумка23 2', 
#                                                            'сумка32 2', 
#                                                            'тетрадь 2', 
#                                                            'альпака 1', 
#                                                            'альпака2 1', 
#                                                            'амулет2 1', 
#                                                            'арбалет 1'])

#       # failed so far --- expected result ['128 6','123 5','124 5','32 5','23 4']
#       inp_list = ['123 5','32 3','124 5','128 1','32 2','23 4','128 4','128 1']
#       self.assertEqual(ex_19_sol.ShopOLAP(8, inp_list), ['128 6','123 5','124 5','32 5','23 4'])
=======
                                                             'бумага 2', 
                                                             'сумка23 2', 
                                                             'сумка32 2', 
                                                             'тетрадь 2'])

        # test 1
        inp_list = ['платье1 5']
        
        self.assertEqual(ex_19_sol.ShopOLAP(5, inp_list), ['платье1 5'])

        # test 2
        inp_list = ['сумка32 2', 
                    'сумка23 2', 
                    'сумка128 4']
        
        self.assertEqual(ex_19_sol.ShopOLAP(5, inp_list),   [
                                                             'сумка128 4', 
                                                             'сумка23 2', 
                                                             'сумка32 2'])

        # test 3
        inp_list = ['сумка32 2', 
                    'сумка23 2', 
                    'сумка128 2']
        
        self.assertEqual(ex_19_sol.ShopOLAP(5, inp_list),   [
                                                             'сумка23 2', 
                                                             'сумка32 2', 
                                                             'сумка128 2'])

        # test 4
        inp_list = ['платье1 5', 
                    'сумка32 2', 
                    'платье1 1', 
                    'сумка23 2', 
                    'бумага 2', 
                    'тетрадь 2', 
                    'сумка128 4', 
                    'альпака 1',
                    'альпака2 1',
                    'арбалет 1',
                    'амулет1 1',
                    'амулет2 1']
        
        self.assertEqual(ex_19_sol.ShopOLAP(5, inp_list),   ['платье1 6', 
                                                             'сумка128 4', 
                                                             'бумага 2', 
                                                             'сумка23 2', 
                                                             'сумка32 2', 
                                                             'тетрадь 2', 
                                                             'альпака 1', 
                                                             'альпака2 1', 
                                                             'амулет1 1', 
                                                             'амулет2 1', 
                                                             'арбалет 1'])

        # test 5
        inp_list = ['платье1 5', 
                    'сумка32 2', 
                    'платье1 1', 
                    'сумка23 2', 
                    'бумага 2', 
                    'тетрадь 2', 
                    'сумка128 4', 
                    'альпака 1',
                    'альпака2 1',
                    'арбалет 1',
                    'амулет1 5',
                    'амулет2 1']
        
        self.assertEqual(ex_19_sol.ShopOLAP(5, inp_list),   ['платье1 6', 
                                                             'амулет1 5', 
                                                             'сумка128 4', 
                                                             'бумага 2', 
                                                             'сумка23 2', 
                                                             'сумка32 2', 
                                                             'тетрадь 2', 
                                                             'альпака 1', 
                                                             'альпака2 1', 
                                                             'амулет2 1', 
                                                             'арбалет 1'])

>>>>>>> next--ex_20

if __name__ == "__main__":
    unittest.main()
