from class_point import Point3D, Point
from random import randint

points_list = []
for i in range(0,5):
    points_list.append(Point(randint(0, 100), randint(0, 100)))
cnt = 1
for i in points_list:
    print(f"Point {cnt}: x = {i.x}, y = {i.y}")
    cnt += 1
