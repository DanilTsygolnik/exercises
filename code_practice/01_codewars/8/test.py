import unittest
from sol import update_light

class Test(unittest.TestCase):

    def test_update_light(self):
        with self.assertRaises(AssertionError):
            update_light(("light in tup"))
        with self.assertRaises(AssertionError):
            update_light("pink")
        self.assertEqual(update_light("green"), "yellow")
        self.assertEqual(update_light("yellow"), "red")
        self.assertEqual(update_light("red"), "green")
        self.assertEqual(update_light("GREEN"), "yellow")
        self.assertEqual(update_light("YELLOW"), "red")
        self.assertEqual(update_light("RED"), "green")

if __name__=="__main__":
    unittest.main()
