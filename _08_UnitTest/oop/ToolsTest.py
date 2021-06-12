import unittest

from context import oop

class MyTestCase(unittest.TestCase):
    def test_knife_can_cut(self):
        knife = oop.Knife()
        can_cut = knife.capability()["cut"]
        self.assertTrue(can_cut)

    def test_knife_cannot_sweep(self):
        knife = oop.Knife()
        can_cut = knife.capability()["sweep"]
        self.assertFalse(can_cut)


if __name__ == '__main__':
    unittest.main()
