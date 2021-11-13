class Point3D:
    """Set a point in space using XYZ coordinates"""

    def __init__(self, x, y, z):
        """ Task 1 """
        self.x = x
        self.y = y
        self.z = z

    def get_coord(self):
        return [self.x, self.y, self.z]
