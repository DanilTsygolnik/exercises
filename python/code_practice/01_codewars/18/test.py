import unittest
from sol import correct

class TestCorrect(unittest.TestCase):
    def test_correct(self):
        self.assertEqual(correct("L0ND0N"), "LONDON")
        self.assertEqual(correct("DUBL1N"), "DUBLIN")
        self.assertEqual(correct("51NGAP0RE"), "SINGAPORE")
        self.assertEqual(correct("BUDAPE5T"), "BUDAPEST")
        self.assertEqual(correct("PAR15"), "PARIS")

if __name__=="__main__":
    unittest.main()
