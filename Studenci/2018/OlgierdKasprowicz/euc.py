#!/usr/bin/env python3
from functools import reduce

def gcd(*numbers):
    """
    Greates common divisor on n args
    """

    if not numbers:
        raise TypeError("At least one argument required!")

    return reduce(gcd_base, numbers)

def gcd_base(a, b=0):
    """
    Greates common divisor on 2 args
    """

    while b != 0:
        a, b = b, a % b 

    return a

def main():
    """
    Primitive test runner, compatible with pytest
    """

    test_functions = [body for name, body in globals().items() if callable(body) and 'test' in name]

    for function in test_functions:
        function()

def test_base():
    assert gcd(100, 50) == 50

def test_one():
    assert gcd(8) == 8

def test_many():
    assert gcd(100, 50, 80, 90, 40, 30) == 10

def test_arg():
    try:
        gcd()
    except TypeError as exception:
        assert exception.args[0] == "At least one argument required!"
    else:
        assert 0

if __name__ == "__main__":
    main()
