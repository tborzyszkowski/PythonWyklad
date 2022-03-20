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
