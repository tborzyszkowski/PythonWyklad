#!/usr/bin/env python3

from math import sqrt

def roots(a,b,c):
    determinant = b ** 2 - 4 * a * c
    determinant_component = sqrt(abs(determinant))

    if determinant < 0:
        determinant_component *= 1j

    return {(-b - determinant_component) / (2 * a), (-b + determinant_component) / (2 * a)} 
def main():
    print(roots(1,2,3))

if __name__ == "__main__":
    main()
