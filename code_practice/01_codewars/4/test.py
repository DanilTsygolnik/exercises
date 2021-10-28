import unittest
from sol import count_sheeps

class Test(unittest.TestCase):

    def test_count_sheeps(self):
        array1 = [True,  True,  True,  False,
                  True,  True,  True,  True ,
                  True,  False, True,  False,
                  True,  False, False, True ,
                  True,  True,  True,  True ,
                  False, False, True,  True ]
        self.assertEqual(count_sheeps(array1), 17)

if __name__=="__main__":
    unittest.main()
