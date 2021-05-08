import unittest
from Point import Point
from math import sqrt

class PointTestCase(unittest.TestCase):

    def test_set_x_positive(self):
        point = Point()
        point.x = 10
        self.assertEqual(10, point.x)

    def test_set_x_negative(self):
        point = Point()
        point.x = -10
        self.assertEqual(10, point.x)

    def test_distance_same_point_is_zero(self):
        point_1 = Point(1, 1)
        point_2 = Point(1, 1)

        result = point_1.distance(point_2)

        self.assertEqual(0, result)

    def test_distance_is_one(self):
        point_1 = Point(1, 1)
        point_2 = Point(1, 2)

        result = point_1.distance(point_2)

        self.assertEqual(1, result)

    def test_distance_is_sqrt2(self):
        point_1 = Point(1, 1)
        point_2 = Point(2, 2)

        result = point_1.distance(point_2)

        self.assertEqual(sqrt(2), result)


if __name__ == '__main__':
    unittest.main()
