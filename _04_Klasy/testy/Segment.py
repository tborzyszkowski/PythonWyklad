from Point import *


class Segment:
    def __init__(self, first_point = Point(0, 0), second_point = Point(1, 1)) -> None:
        self.first_point = first_point
        self.second_point = second_point

    @property
    def first_point(self):
        return self.__first_point

    @first_point.setter
    def first_point(self, first_point):
        self.__first_point = first_point

    def length(self):
        return self.first_point.distance(self.second_point)
