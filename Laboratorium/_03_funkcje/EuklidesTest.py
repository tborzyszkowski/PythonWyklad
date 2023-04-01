import unittest
from Laboratorium._03_funkcje.Euklides import *


class EuklidesTest(unittest.TestCase):
    def test_for_two_prime_numbers(self):
        # Arrange
        first_number = 7
        second_number = 13
        # Act
        actual_value = euklides(first_number, second_number)
        # Assert
        self.assertEqual(1, actual_value)

    def test_for_two_numbers(self):
        # Arrange
        first_number = 1024
        second_number = 256
        # Act
        actual_value = euklides(first_number, second_number)
        # Assert
        self.assertEqual(256, actual_value)

    def test_for_two_big_composed_numbers(self):
        first_prime_number = 64781
        second_prime_number = 68041
        third_prime_number = 71429
        actual_value = euklides(
            first_prime_number * second_prime_number,
            second_prime_number * third_prime_number
        )
        self.assertEqual(second_prime_number, actual_value)

    def test_for_negative_number(self):
        first_number = 36
        second_number = -18
        actual_value = euklides(first_number, second_number)
        self.assertEqual(18, actual_value)

    def test_for_zero(self):
        first_number = 0
        second_number = 18
        actual_value = euklides(first_number, second_number)
        self.assertEqual(-1, actual_value)


class EuklidesMultiTest(unittest.TestCase):
    def test_for_three_numbers(self):
        list_of_numbers = [12, 16, 36]
        actual_value = euklides_multi(*list_of_numbers)
        self.assertEqual(4, actual_value)

    def test_for_one_numbers(self):
        list_of_numbers = [8]
        actual_value = euklides_multi(*list_of_numbers)
        self.assertEqual(8, actual_value)

    def test_for_no_numbers(self):
        list_of_numbers = []
        with self.assertRaises(TypeError):
            euklides_multi(*list_of_numbers)


if __name__ == "__main__":
    unittest.main()
