import unittest

from context import oop

class SegmentTestCase(unittest.TestCase):
    def test_distance_zero_segment(self):
        segment = oop.Segment(oop.Point(1, 1), oop.Point(1, 1))
        distance = segment.length()
        self.assertEqual(0, distance)

    def test_distance_one_segment(self):
        segment = oop.Segment(oop.Point(1, 1), oop.Point(2, 1))
        distance = segment.length()
        self.assertEqual(1, distance)


if __name__ == '__main__':
    unittest.main()
