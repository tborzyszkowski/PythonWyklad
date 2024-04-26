import unittest

from Laboratorium._04_klasy.Geometry.Point import Point


class PointTest(unittest.TestCase):
    def test_set_x_positive_value(self):
        p = Point()
        value = 1
        p.x = value
        self.assertEqual(p.x, value)

    def test_set_x_negative_value_raises_exception(self):
        p = Point()
        value = -1
        with self.assertRaises(Exception):
            p.x = value

    def test_set_y_positive_value(self):
        p = Point()
        value = 1
        p.y = value
        self.assertEqual(p.y, value)

    def test_set_y_negative_value_gives_positive(self):
        p = Point()
        value = -1
        p.y = value
        self.assertEqual(-value, p.y)

    def test_distance_one(self):
        point1 = Point(0, 0)
        point2 = Point(1, 0)
        result = point1.distance(point2)
        self.assertEqual(1, result)

    def test_is_valid_having_one_return_true(self):
        value = 1
        result = Point.is_valid(value)
        self.assertTrue(result)

    def test_is_valid_having_minus_one_return_false(self):
        value = -1
        result = Point.is_valid(value)
        self.assertFalse(result)

