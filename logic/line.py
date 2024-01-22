from logic.point import Point

from math import sqrt

class Line:
    def __init__(self, point1: Point, point2: Point) -> None:
        if point1.x == point2.x and point1.y == point2.y:
            raise ValueError('Точка не является прямой. Координаты точек не должны совпадать.')
        self.__start_point : Point = point1
        self.__end_point : Point = point2

    @property
    def start_point(self) -> Point:
        return self.__start_point
    
    @start_point.setter
    def start_point(self, point: Point) -> None:
        if self.__end_point.x == point.x and self.__end_point.y == point.y:
            raise ValueError('Координаты начальной точки не должны совпадать с координатами конечной точки.')
        self.__start_point = point

    @property
    def end_point(self)-> Point:
        return self.__end_point
    
    @end_point.setter
    def end_point(self, point: Point) -> None:
        if self.__start_point.x == point.x and self.__start_point.y == point.y:
            raise ValueError('Координаты конечной точки не должны совпадать с координатами начальной точки.')
        self.end_point = point

    def set_start_coordinates(self, x: int, y: int) -> None:
        self.start_point = Point(x, y)

    def set_end_coordinates(self, x: int, y: int) -> None:
        self.end_point = Point(x, y)

    def length(self) -> float:
        return sqrt(
            (self.__start_point.x - self.__end_point.x)**2 +
            (self.__start_point.y - self.__end_point.y)**2)