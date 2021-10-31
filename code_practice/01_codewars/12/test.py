import unittest
from sol import rental_car_cost

class Test(unittest.TestCase):

    def test_(self):
        self.assertEqual(rental_car_cost(0),0)
        self.assertEqual(rental_car_cost(1),40)
        self.assertEqual(rental_car_cost(4),140)
        self.assertEqual(rental_car_cost(7),230)
        self.assertEqual(rental_car_cost(8),270)

if __name__=="__main__":
    unittest.main()
