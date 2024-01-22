from unittest import TestCase

from logic.line3d import Line3D
from logic.point3d import Point3D



class TestInit(TestCase):

    def test_init_01(self):
        point1 = Point3D(0,0,0)
        point2 = Point3D(0,0,1)
        line = Line3D(point1, point2)

    def test_init_02(self):
        point1 = Point3D(0,0,0)
        point2 = Point3D(0,0,0)
        self.assertRaises(ValueError, Line3D, point1, point2)