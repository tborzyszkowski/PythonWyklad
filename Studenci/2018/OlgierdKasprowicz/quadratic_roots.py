#!/usr/bin/env python3
"""
The purpose of these programme is to compute roots (including complex roots)
of a normalized quadaric equation.

Notes:
- Actually the quadatic expression / equation should be represented by a class,
but the classess were not yet part of the Python course
- Excessive comments were added for educational purposes
"""

# Math for complex numbers - hence the "c"
from cmath import sqrt

# A cool container which properties can be accessed like it was an object
from collections import namedtuple


# representing ()x^2 + ()x + () == 0
NormalQuadraticEquation = namedtuple('QuadraticFactors',
    [
        'square_coefficient',
        'linear_coefficient',
        'free_term',
    ])

# No need for bloated docstring as we have type annotations!
def roots_of(factors: NormalQuadraticEquation) -> {float}:
    # Actually there is no need for any docstring as this function is self-explanatory!

    # The formulas are easier to read with commonly used labels 
    a = factors.square_coefficient 
    b = factors.linear_coefficient 
    c = factors.free_term 

    determinant = b**2 - 4*a*c

    # No need for "nifty" checks as we operate in complex number domain
    determinant_component = sqrt(determinant)

    # Set takes care of any duplicates
    return {
        (-b - determinant_component) / 2*a,
        (-b + determinant_component) / 2*a,
    }


def main():
    # see WolfamAlpha to verify if the outputs are correct

    # https://www.wolframalpha.com/input/?i=x%5E2%2B2x%2B3%3D0 
    print(roots_of(NormalQuadraticEquation(1, 2, 3)))

    # https://www.wolframalpha.com/input/?i=x%5E2%2B2x%2B1%3D0
    print(roots_of(NormalQuadraticEquation(1, 2, 1)))

    # https://www.wolframalpha.com/input/?i=3x%5E2%2B2x-1%3D0
    print(roots_of(NormalQuadraticEquation(3, 2, -1)))
    

if __name__ == "__main__":
    main()
