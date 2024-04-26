import unittest
from unittest.mock import Mock

from Laboratorium._04_klasy.Geometry.Point import Point
from Laboratorium._04_klasy.Geometry.Segment import Segment


class SegmentTest(unittest.TestCase):
    def test_isvalid_true(self):
        point = Mock(Point)
        point.distance.return_value = 2
        result = Segment.is_valid(point)
        self.assertTrue(result)

    def test_isvalid_true(self):
        point = Mock(Point)
        point.distance.return_value = 0
        result = Segment.is_valid(point)
        self.assertFalse(result)

