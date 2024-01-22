from logic.point3d import Point3D
from logic.line import Line


class Line3D(Line):
    
    def __init__(self, p1: Point3D, p2: Point3D):
        if p1.x == p2.x and p1.y ==p2.y and p1.z == p2.z:
            raise ValueError('Точка не является прямой. Координаты точек не должны совпадать.')
        self.__start_point = p1
        self.__end_point = p2


    