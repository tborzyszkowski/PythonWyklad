import unittest

from Laboratorium._04_klasy.Geometry.Point import Point
from Laboratorium._04_klasy.Geometry.Segment import Segment


class SegmentTest(unittest.TestCase):
    def test_start(self):
        point_start = Point(1, 1)
        segment = Segment(point_start)

        self.assertEqual(segment.start.x, 1)

    def test_start_negative(self):
        point_start = Point(-1, 1)
        segment = Segment(point_start)

        self.assertEqual(segment.start.x, 0)

