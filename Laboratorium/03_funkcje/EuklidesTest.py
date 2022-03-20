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
        self.assertEqual(1, actual_value)

    def test_for_two_big_composed_numbers(self):
        first_prime_number = 64781
        second_prime_number = 68041
        third_prime_number = 71429
        actual_value = Euklides.euklides(
            first_prime_number * second_prime_number,
            second_prime_number * third_prime_number
        )
        self.assertEqual(second_prime_number, actual_value)

    def test_for_negative_number(self):
        first_number = 36
        second_number = -18
        actual_value = Euklides.euklides(first_number, second_number)
        self.assertEqual(18, actual_value)

    def test_for_zero(self):
        first_number = 0
        second_number = 18
        actual_value = Euklides.euklides(first_number, second_number)
        self.assertEqual(-1, actual_value)


class EuklidesMultiTest(unittest.TestCase):
    def test_for_two_prime_numbers(self):
        list_of_numbers = [12, 16, 36]
        actual_value = Euklides.euklides_multi(*list_of_numbers)
        self.assertEqual(4, actual_value)



if __name__ == "__main__":
    unittest.main()
