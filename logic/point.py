class Point:
    def __init__(self, x: int, y: int) -> None:
        self.__x = x
        self.__y = y
    
    @property
    def x(self) -> int:
        return self.__x

    @x.setter
    def x(self, value: int) -> None:
        self.__x = value
    
    @property
    def y(self) -> int:
        return self.__y
    
    @y.setter
    def y(self, value: int) -> None:
        self.__y = value
    
    def set_coordinates(self, x: int, y: int) -> None:
        self.__x = x
        self.__y = y

    def get_coordinates(self) -> tuple:
        return self.__x, self.__y