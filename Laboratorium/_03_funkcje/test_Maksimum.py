from Laboratorium._03_funkcje import Maksimum


class TestMaksimum:
    def test_max1_1_2_is_2(self):
        arg_1 = 1
        arg_2 = 2
        expected = 2
        result = Maksimum.max1(arg_1, arg_2)
        assert result == expected

    def test_max1_10_151_is_151(self):
        arg_1 = 10
        arg_2 = 151
        expected = 151
        result = Maksimum.max1(arg_1, arg_2)
        assert result == expected

    def test_max1_2_1_is_2(self):
        arg_1 = 2
        arg_2 = 1
        expected = 2
        result = Maksimum.max1(arg_1, arg_2)
        assert result == expected

    def test_max1_151_10_is_151(self):
        arg_1 = 151
        arg_2 = 10
        expected = 151
        result = Maksimum.max1(arg_1, arg_2)
        assert result == expected

