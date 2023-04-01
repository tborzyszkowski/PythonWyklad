from Laboratorium._03_funkcje.Euklides import *

class TestClass:
    def test_1_isPrime(self):
        # Arrange
        argument = 1
        #Act
        result = is_prime(argument)
        #Assert
        assert result

    def test_4_isNotPrime(self):
        argument = 4
        result = is_prime(argument)
        assert not result

    def test_euklides_multi_on_12_6_4_is_2(self):
        lista_argumentow = [12, 6, 4]
        result = euklides_multi(*lista_argumentow)
        assert result == 2