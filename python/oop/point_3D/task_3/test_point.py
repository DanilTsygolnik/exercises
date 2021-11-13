import unittest
from class_point import Point3D, Point

class TestPoint3D(unittest.TestCase):
    
    def setUp(self):
        self.pt = Point3D()

    def test_main(self):
        self.assertEqual(self.pt.getCoord(), (0,0,0))
        self.pt.setCoord("x", 1)
        self.assertEqual(self.pt.getCoord(), (1,0,0))

class TestPoint(unittest.TestCase):
    
    def setUp(self):
        self.pt = Point()

    def test_main(self):
        self.assertEqual(self.pt.getCoord(), (0,0))
        pt3D = Point3D(3,4,5)
        self.pt = Point(pt3D)
        self.assertEqual(self.pt.getCoord(), (3,4))


if __name__=="__main__":
    unittest.main()
