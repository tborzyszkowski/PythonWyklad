from math import sqrt

class Point:
    def __init__(self, x_coordinate = 0, y_coordinate = 0) -> None:
        self.x = x_coordinate
        self.y = y_coordinate

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, x):
        self.__x = x if x >= 0 else -x

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, y):
        self.__y = y if y >= 0 else -y

    def distance(self, point):
        return sqrt((self.x - point.x) ** 2 + (self.y - point.y) ** 2)

