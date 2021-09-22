import unittest
import ex_1_sol

class TestEx_1(unittest.TestCase):

    def test_squirrel(self):
        # N >= 0 -- ValueError in squirrel(N)
        self.assertRaises(ValueError, ex_1_sol.squirrel, -5)
        # int -- ValueError in squirrel(N)
        self.assertRaises(ValueError, ex_1_sol.squirrel, 2.3)
        #with self.assertRaises(ValueError):
        #    ex_1_sol.squirrel(2.3)
        self.assertEqual(ex_1_sol.squirrel(0), 1)
        self.assertEqual(ex_1_sol.squirrel(1), 1)
        self.assertEqual(ex_1_sol.squirrel(2), 2)
        self.assertEqual(ex_1_sol.squirrel(3), 6)
        self.assertEqual(ex_1_sol.squirrel(4), 2)
        self.assertEqual(ex_1_sol.squirrel(5), 1)
        self.assertEqual(ex_1_sol.squirrel(6), 7)
        self.assertEqual(ex_1_sol.squirrel(7), 5)
        self.assertEqual(ex_1_sol.squirrel(8), 4)
        self.assertEqual(ex_1_sol.squirrel(9), 3)
        self.assertEqual(ex_1_sol.squirrel(10), 3)
        self.assertEqual(ex_1_sol.squirrel(11), 3)

    #def test_emeralds(self):
    #    self.assertEqual(ex_1_sol.emeralds(0), 0)
    #    self.assertEqual(ex_1_sol.emeralds(5), 5)
    #    self.assertEqual(ex_1_sol.emeralds(1024), 1)
    #
    #def test_factorital(self):
    #    self.assertEqual(ex_1_sol.fact(0), 1)
    #    self.assertEqual(ex_1_sol.fact(1), 1)
    #    self.assertEqual(ex_1_sol.fact(2), 2)
    #    self.assertEqual(ex_1_sol.fact(3), 6)
    #    self.assertEqual(ex_1_sol.fact(4), 24)
    #    self.assertEqual(ex_1_sol.fact(5), 120)
    #    self.assertEqual(ex_1_sol.fact(6), 720)
    #    self.assertEqual(ex_1_sol.fact(7), 5040)
    #    self.assertEqual(ex_1_sol.fact(8), 40320)
    #    self.assertEqual(ex_1_sol.fact(9), 362880)
    #    self.assertEqual(ex_1_sol.fact(10), 3628800)
    #    self.assertEqual(ex_1_sol.fact(11), 39916800)

if __name__ == "__main__":
    unittest.main()
