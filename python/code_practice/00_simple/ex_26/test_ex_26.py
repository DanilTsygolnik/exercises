# pylint: disable=c0103,c0114,c0115,c0116
import unittest
import ex_26_sol

class Test_ex_26_sol(unittest.TestCase):

    def test_get_all_pairs(self):
        self.assertEqual(ex_26_sol.get_all_pairs("5==ooooooo"), [])
        self.assertEqual(ex_26_sol.get_all_pairs("abc=7==hdj"), [])
        self.assertEqual(ex_26_sol.get_all_pairs("axxb6===4x"), [[6,4]])
        self.assertEqual(ex_26_sol.get_all_pairs("9===1===9="), [[9,1], [1,9]])

    def test_get_all_indexes(self):
        #  0123456789
        # "5==ooooooo" --> []
        # "abc=7==hdj" --> []
        # "axxb6===4x" --> [[5,8]]
        # "9===1===9=" --> [[1,4], [5,8]]

        self.assertEqual(ex_26_sol.get_all_indexes("5==ooooooo"), [])
        self.assertEqual(ex_26_sol.get_all_indexes("abc=7==hdj"), [])
        self.assertEqual(ex_26_sol.get_all_indexes("axxb6===4x"), [[5,8]])
        self.assertEqual(ex_26_sol.get_all_indexes("9===1===9="), [[1,4], [5,8]])

    def test_choose_pairs(self):
        self.assertEqual(ex_26_sol.choose_pairs("5==ooooooo"), [])
        self.assertEqual(ex_26_sol.choose_pairs("abc=7==hdj"), [])
        self.assertEqual(ex_26_sol.choose_pairs("axxb6===4x"), [[5,8]])
        self.assertEqual(ex_26_sol.choose_pairs("9===1===9="), [[1,4], [5,8]])
        self.assertEqual(ex_26_sol.choose_pairs("6===4xa===f5===eee6==afada=4"), [[1,4], [19,27]])

    def test_amount_is_there(self):
        self.assertFalse(ex_26_sol.amount_is_there(target="=", location=""))
        self.assertFalse(ex_26_sol.amount_is_there(target="=", location="abcd"))
        self.assertFalse(ex_26_sol.amount_is_there(target="=", location="==ooo"))
        self.assertFalse(ex_26_sol.amount_is_there(target="=", location="====="))
        self.assertFalse(ex_26_sol.amount_is_there(target="=", location="axxb6=====4x"))

        self.assertTrue(ex_26_sol.amount_is_there(target="=", location="axxb6===4x"))
        self.assertTrue(ex_26_sol.amount_is_there(target="=", location="axxb6======4x"))

    def test_white_walkers(self):
        self.assertTrue(ex_26_sol.white_walkers("axxb6===4xaf5===eee5"))
        self.assertTrue(ex_26_sol.white_walkers("abc=7==hdjs=3gg1=======5"))
        self.assertTrue(ex_26_sol.white_walkers("9===1===9===1===9"))
        self.assertTrue(ex_26_sol.white_walkers("9=cd==1==ab=9=e==1=f=g=9"))
        self.assertTrue(ex_26_sol.white_walkers("axxb6===4xaf5===eee6"))
        self.assertTrue(ex_26_sol.white_walkers("axxb6===4"))
        self.assertTrue(ex_26_sol.white_walkers("6===4"))
        self.assertTrue(ex_26_sol.white_walkers("6===4xa===f5===eee6==afada=4"))

        self.assertFalse(ex_26_sol.white_walkers(""))
        self.assertFalse(ex_26_sol.white_walkers("aaS=8"))
        self.assertFalse(ex_26_sol.white_walkers("6==4"))
        self.assertFalse(ex_26_sol.white_walkers("6===4xa===f5===eee6==afada4"))
        self.assertFalse(ex_26_sol.white_walkers("5==ooooooo=5=5"))
        self.assertFalse(ex_26_sol.white_walkers("9abc1===9===1===9"))
        self.assertFalse(ex_26_sol.white_walkers("9==1===9===1===9"))
        self.assertFalse(ex_26_sol.white_walkers("axxb6===4xaf6===eee5"))

        # ??????-???? "=" ???????????? ???????? ???????????? 3
        self.assertFalse(ex_26_sol.white_walkers("6====4"))
        self.assertFalse(ex_26_sol.white_walkers("9====1===9===1===9"))


if __name__ == "__main__":
    unittest.main()
