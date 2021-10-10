import unittest
import ex_20_sol

class Test_ex_20_sol(unittest.TestCase):

    def test_S_is_number(self):
        
        self.assertTrue(ex_20_sol.S_is_number('5'))
        self.assertFalse(ex_20_sol.S_is_number('xx'))

    def test_BastShoe(self):
        
        commands = [
                        '1 Привет', 
                        '1 , Мир!', 
                        '1 ++ ', 
                        '2 2', 
                        '4', 
                        '4', 
                        '1 *', 
                        '4', 
                        '4 ', 
                        '4', 
                        '3 6', 
                        '2 100', 
                        '1 Привет', 
                        '1 , Мир!', 
                        '1 ++ ', 
                        '4', 
                        '4', 
                        '5', 
                        '4', 
                        '5', 
                        '5', 
                        '5', 
                        '5', 
                        '4', 
                        '4', 
                        '2 2', 
                        '4', 
                        '5', 
                        '5', 
                        '5']

        answers = [

                        'Привет', 
                        'Привет, Мир!', 
                        'Привет, Мир!++', 
                        'Привет, Мир!', 
                        'Привет, Мир!++', 
                        'Привет, Мир!', 
                        'Привет, Мир!*', 
                        'Привет, Мир!', 
                        'Привет, Мир!', 
                        'Привет, Мир!', 
                        ',', 
                        '', 
                        'Привет', 
                        'Привет, Мир!', 
                        'Привет, Мир!++', 
                        'Привет, Мир!', 
                        'Привет', 
                        'Привет, Мир!', 
                        'Привет', 
                        'Привет, Мир!', 
                        'Привет, Мир!++', 
                        'Привет, Мир!++', 
                        'Привет, Мир!++', 
                        'Привет, Мир!', 
                        'Привет', 
                        'Прив', 
                        'Привет', 
                        'Прив', 
                        'Прив', 
                        'Прив']

        # BastShoe test
        ans_BastShoe=[]

        for i in commands:
            ans_BastShoe.append(ex_20_sol.BastShoe(i))
        self.assertEqual(ans_BastShoe, answers)


if __name__ == "__main__":
    unittest.main()
