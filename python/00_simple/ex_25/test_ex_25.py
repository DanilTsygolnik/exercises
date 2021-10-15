import unittest
import ex_25_sol

class Test_ex_25_sol(unittest.TestCase):

    def test_transform(self):
        # ================== common case ====================
        # step 1
        #     i 0 1 2 3 4  i=0, len(data)-i-1 = 4, j=[0..3]
        #       j 0 1 2 3
        #       k 0 1 2 3
        # Диапазоны поиска max(), [j,k+1]:
        #    [0:1] [1:2] [2:3] [3:4]
        #  ---------------------------------------------------
        # step 2
        #     i 0 1 2 3 4  i=1, len(data)-i-1 = 3, j=[0..2]
        #         j 0 1 2
        #         k 1 2 3
        # Диапазоны поиска max(), [j,k+1]:
        #    [0:2] [1:3] [2:4]
        #  ---------------------------------------------------
        # step 3
        #     i 0 1 2 3 4  i=2, len(data)-i-1 = 2, j=[0..1]
        #           j 0 1
        #           k 2 3
        # Диапазоны поиска max(), [j,k+1]:
        #    [0:3] [1:4]
        #  ---------------------------------------------------
        # step 4
        #     i 0 1 2 3 4  i=3, len(data)-i-1 = 1, j=[0]
        #             j 0
        #             k 3
        # Диапазоны поиска max(), [j,k+1]:
        #    [0:4]
        #  ---------------------------------------------------
        # step 5
        #     i 0 1 2 3 4  i=4, len(data)-i-1 = 0, j in range(0,0) ??
        #               j ?? ==> k=i=4
        # Поиск не требуется, выводится единственное значение data[i]
        # ____________________________________________________
        #     i 0 1 2 3 4
        data = [1,2,3,4,5]
        # step 1 --> [1, 2, 3, 4]
        # step 2 --> [1, 2, 3, 4, 2, 3, 4]
        # step 3 --> [1, 2, 3, 4, 2, 3, 4, 3, 4]
        # step 4 --> [1, 2, 3, 4, 2, 3, 4, 3, 4, 4]
        # step 5 --> ref
        ref = [1, 2, 3, 4, 2, 3, 4, 3, 4, 4, 5]
        # common case test
        self.assertEqual(ex_25_sol.transform(data), ref)

        # ================== edge cases tests =================
        self.assertEqual(ex_25_sol.transform([]), [])
        self.assertEqual(ex_25_sol.transform([666]), [666])

    def test_get_master_key(self):
        data_transformed = ex_25_sol.transform([1,2,3,4,5])
        data_double_transformed = ex_25_sol.transform(data_transformed)
        ref = sum(data_double_transformed)
        self.assertEqual(ex_25_sol.get_master_key([1,2,3,4,5]), ref)

    def test_TransformTransform(self):
    
        self.assertTrue(ex_25_sol.TransformTransform([1,2,3,4], 4))
        self.assertFalse(ex_25_sol.TransformTransform([1,2,3,5], 4))


if __name__ == "__main__":
    unittest.main()
