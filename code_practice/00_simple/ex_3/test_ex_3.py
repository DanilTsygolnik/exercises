import unittest
import ex_3_sol

class TestEx_3(unittest.TestCase):

    def test_ConquestCampaign(self):
        self.assertEqual(ex_3_sol.ConquestCampaign(3, 4, 2, [2, 2, 3, 4]), 3)
        self.assertEqual(ex_3_sol.ConquestCampaign(1, 1, 1, [1, 1]), 1)
        self.assertEqual(ex_3_sol.ConquestCampaign(1, 2, 1, [1, 1]), 2)
        self.assertEqual(ex_3_sol.ConquestCampaign(2, 2, 2, [1, 1, 2, 2]), 2)
        self.assertEqual(ex_3_sol.ConquestCampaign(2, 2, 1, [1, 1]), 3)
        self.assertEqual(ex_3_sol.ConquestCampaign(3, 3, 1, [1, 1]), 5)
        self.assertEqual(ex_3_sol.ConquestCampaign(3, 3, 3, [1, 1, 2, 2, 3, 3]), 3)
        self.assertEqual(ex_3_sol.ConquestCampaign(3, 3, 6, [1, 1, 2, 2, 3, 3, 2, 2, 3, 3, 1, 1]), 3)
        self.assertEqual(ex_3_sol.ConquestCampaign(4, 4, 1, [1, 1]), 7)
        self.assertEqual(ex_3_sol.ConquestCampaign(4, 4, 3, [3, 1, 4, 4, 1, 4]), 3)
        self.assertEqual(ex_3_sol.ConquestCampaign(5, 5, 5, [3, 3, 1, 1, 5, 2, 1, 1, 3, 3]), 5)

if __name__ == "__main__":
    unittest.main()
