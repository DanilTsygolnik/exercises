class Point3D:
    def __init__(self, x: float = 0, y: float = 0, z: float = 0):
        self.x = x
        self.y = y
        self.z = z

    def setCoord(self, coord:str, value):
        if coord == "x":
            self.x = value
        if coord == "y":
            self.y = value
        if coord == "z":
            self.z = value

    def getCoord(self):
        return (self.x, self.y, self.z)

class Point:
    def __init__(self, x=0, y=0, point=None):
        self.x = x
        self.y = y
        if point is not None:
            self.x = point.x
            self.y = point.y

    def getCoord(self):
        return (self.x, self.y)
