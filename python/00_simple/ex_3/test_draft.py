import unittest
import draft

class TestEx_3_Draft(unittest.TestCase):

    def test_add_pair(self):
        target = {}
        t_values_list = []
        checklist = []
        for i in range(0, 35, 5):
            draft.add_pair(i + 1, i + 3, target)
            checklist.append([i + 1, i + 3])
        for v in target.values():
            t_values_list.append(v)

        # output values
        self.assertEqual(checklist, t_values_list)

    def test_uniqueList(self):
        v_list1 = [1, 1, 2, 2, 3, 3]
        v_list2 = [1, 1, 2, 2, 3, 3, 2, 2, 3, 3, 1, 1]
        t_dict1 = {}
        t_dict2 = {}
        checklist = [[1, 1], [2, 2], [3, 3]]
        t_dict_val1 = []
        t_dict_val2 = []
        draft.uniqueList(v_list1, t_dict1)
        for v in t_dict1.values():
            t_dict_val1.append(v)
        draft.uniqueList(v_list2, t_dict2)
        for v in t_dict2.values():
            t_dict_val2.append(v)
        # output values
        self.assertEqual(checklist, t_dict_val1)
        self.assertEqual(checklist, t_dict_val2)

    def test_ConquestCampaign(self):
        self.assertEqual(draft.ConquestCampaign(3, 4, 2, [2, 2, 3, 4]), 3)
        self.assertEqual(draft.ConquestCampaign(1, 1, 1, [1, 1]), 1)
        self.assertEqual(draft.ConquestCampaign(1, 2, 1, [1, 1]), 2)
        self.assertEqual(draft.ConquestCampaign(2, 2, 2, [1, 1, 2, 2]), 2)
        self.assertEqual(draft.ConquestCampaign(2, 2, 1, [1, 1]), 3)
        self.assertEqual(draft.ConquestCampaign(3, 3, 1, [1, 1]), 5)
        self.assertEqual(draft.ConquestCampaign(3, 3, 3, [1, 1, 2, 2, 3, 3]), 3)
        self.assertEqual(draft.ConquestCampaign(3, 3, 6, [1, 1, 2, 2, 3, 3, 2, 2, 3, 3, 1, 1]), 3)
        self.assertEqual(draft.ConquestCampaign(4, 4, 1, [1, 1]), 7)
        self.assertEqual(draft.ConquestCampaign(4, 4, 3, [3, 1, 4, 4, 1, 4]), 3)
        self.assertEqual(draft.ConquestCampaign(5, 5, 5, [3, 3, 1, 1, 5, 2, 1, 1, 3, 3]), 5)
        

if __name__ == "__main__":
    unittest.main()
