import unittest
from Laboratorium._01_start._022_fibonacci import fibonacci

class FibonacciTestCase(unittest.TestCase):
    def test_fib_1_1(self):
        value = 1
        expected = 1
        result = fibonacci(value)
        self.assertEqual(result, expected)

    def test_fib_2_1(self):
        value = 2
        expected = 1
        result = fibonacci(value)
        self.assertEqual(result, expected)

    def test_fib_5_5(self):
        value = 5
        expected = 5
        result = fibonacci(value)
        self.assertEqual(result, expected)

    def test_fib_19_4181(self):
        value = 19
        expected = 4181
        result = fibonacci(value)
        self.assertEqual(result, expected)

    def test_fib_m1_m1(self):
        value = -1
        expected = -1
        result = fibonacci(value)
        self.assertEqual(result, expected)


if __name__ == '__main__':
    unittest.main()
