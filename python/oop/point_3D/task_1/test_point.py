import unittest
from class_point import Point3D

class TestPoint3D(unittest.TestCase):
    
    def test(self):

        ref = [[1,2,3], [4,5,6], [7,8,9]]
        points = []
        cnt = 1
        for i in ref:
            exec(f"pt{cnt} = Point3D({i[0]},{i[1]},{i[2]})")
            exec(f"points.append(pt{cnt})")
            cnt += 1
        cnt = 0
        for i in points:
            self.assertEqual(i.get_coord(), ref[cnt])
            cnt += 1

        # task 2
        pt2D = points[0]
        delattr(pt2D, "z")
        self.assertFalse(hasattr(pt2D, "z"))
        self.assertTrue(hasattr(points[1], "z"))
        self.assertTrue(hasattr(points[2], "z"))

        test_pt = points[2]
        print(test_pt.__dict__)
        test_pt.y = 7
        test_pt.z = 7
        self.assertEqual(test_pt.get_coord(), [7,7,7])
        print(test_pt.__dict__)

if __name__=="__main__":
    unittest.main()
