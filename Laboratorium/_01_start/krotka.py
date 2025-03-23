from functools import reduce

import pytest


def tuple_processing(my_tuple):
    if isinstance(my_tuple, tuple):
        if len(my_tuple) == 2:
            if reduce((lambda x, y: x and y), [ isinstance(element, str) for element in my_tuple ], True):
                return my_tuple
            else:
                return "reduce"
        else:
            return "Len != 2"
    else:
        return "no tuple"

def test_not_tuple():
    assert tuple_processing(1) == "no tuple"

def test_not_tuple():
    assert tuple_processing((1, 2)) == "reduce"


if __name__ == '__main__':
    pytest.main()