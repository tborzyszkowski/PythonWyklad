import unittest
import Euklides

class EuklidesTest(unittest.TestCase):
    def test_for_two_prime_numbers(self):
        # Arrange
        first_number = 7
        second_number = 13
        # Act
        actual_value = Euklides.euklides(first_number, second_number)
        # Assert
        self.assertEqual(2, actual_value)

    def test_for_two_big_composed_numbers(self):
        # Arrange
        first_prime_number = 64781
        second_prime_number = 68041
        third_prime_number = 71429
        # Act
        actual_value = Euklides.euklides(
            first_prime_number * second_prime_number,
            second_prime_number * third_prime_number
        )
        # Assert
        self.assertEqual(second_prime_number, actual_value)

