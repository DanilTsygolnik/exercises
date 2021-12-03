import unittest
from power import raise_to_power

class TestFunc(unittest.TestCase):
    
    def test_main(self):
        
        for i in [-5, 0, 5]:
            self.assertEqual(raise_to_power(i, 0), i**0)
            self.assertEqual(raise_to_power(i, 1), i**1)
            self.assertEqual(raise_to_power(i, 3), i**3)
            if i == 0:
                with self.assertRaises(ZeroDivisionError):
                    raise_to_power(i,-1)
            else:
                self.assertEqual(raise_to_power(i,-1), i**(-1))
                self.assertEqual(raise_to_power(i,-3), i**(-3))

if __name__=="__main__":
    unittest.main()
