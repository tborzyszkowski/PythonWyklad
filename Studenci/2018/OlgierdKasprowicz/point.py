#!/usr/bin/env python3
from math import sqrt


class Point():
    def __init__(self, *coordinates):
        self.coordinates = coordinates

    def distance(self, other):
        """
        The dimentions are floored if not equal
        """
        return sqrt(sum({(xi - xj) ** 2 for xi, xj in zip(self.coordinates, other.coordinates)}))
     

def main():
    pass


def test_same_points():
    p = Point(1,1)
    q = Point(1,1)

    assert p.distance(q) == 0


def test_different_points():
    p = Point(1)
    q = Point(0)

    assert p.distance(q) == 1


def test_alteration():
    p = Point(1)
    q = Point(0)

    assert p.distance(q) == q.distance(p)


    

if __name__ == "__main__":
    main()
