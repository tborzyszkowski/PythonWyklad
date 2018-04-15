#!/usr/bin/env python3
from point import Point

class Mockingbird():
    """
    Mockingbird sings and mocks other objects
    """

    def __init__(self, message): 
        self.message = message
        self.__message = message

    def sing(self):
        print("Hello {}".format(self.message))

    def safe_sing(self):
        print("Hello {}".format(self.__message))

    def mock(self, cls, *args, **kwargs):
        cls.__init__(self, *args, **kwargs)


class A():
    def __init__(self):
        self.message = "A"


def main():
    m = Mockingbird("John")

    # ----

    m.mock(Point, 1, 1)
    p = Point(1,1)

    m.sing()
    print(Point.distance(m, p))

    # ----

    m.sing()
    m.safe_sing()

    m.mock(A)

    m.sing()
    m.safe_sing()

if __name__ == "__main__":
    main()
