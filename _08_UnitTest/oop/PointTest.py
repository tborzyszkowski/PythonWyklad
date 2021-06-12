import unittest

from context import oop

class PointTestCase(unittest.TestCase):

    def test_set_x_positive(self):
        point = oop.Point()
        point.x = 10
        self.assertEqual(11, point.x)

    def test_set_x_negative(self):
        point = oop.Point()
        point.x = -10
        self.assertEqual(10, point.x)



if __name__ == '__main__':
    unittest.main()
