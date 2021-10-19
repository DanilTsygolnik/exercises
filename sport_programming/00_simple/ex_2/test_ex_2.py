import unittest
import ex_2_sol

class TestEx_1(unittest.TestCase):

    def test_odometr(self):
	# wrong arguments
        #self.assertRaises(ValueError, ex_2_sol.odometer, 666)
        #self.assertRaises(ValueError, ex_2_sol.odometer, [65])
        #self.assertRaises(ValueError, ex_2_sol.odometer, [-24, 65])
        #self.assertRaises(ValueError, ex_2_sol.odometer, [35.6, 65])
	# output values
        self.assertEqual(ex_2_sol.odometer([0, 0]), 0)
        self.assertEqual(ex_2_sol.odometer([10, 1, 20]), 10)
        self.assertEqual(ex_2_sol.odometer([10, 1, 20, 2]), 30)
        self.assertEqual(ex_2_sol.odometer([10, 1, 20, 2, 40, 4]), 110)
        self.assertEqual(ex_2_sol.odometer([10, 1, 20, 2, 40, 4, 50]), 110)

if __name__ == "__main__":
    unittest.main()
