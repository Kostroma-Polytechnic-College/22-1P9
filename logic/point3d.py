from logic.point import Point

class Point3D(Point):
    def __init__(self, x:int, y:int, z:int) -> None:
        super().__init__(x, y)
        self.__z = z

    @property
    def z(self) -> int:
        return self.__z
    
    @z.setter
    def z(self, value: int) -> None:
        self.__z = value

    def get_coordinates(self) -> tuple:
        return *super().get_coordinates(), self.__z
    
    def set_coordinates(self, x: int, y: int, z: int) -> None:
        super().set_coordinates(x, y)
        self.__z = z