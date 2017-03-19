import math

# x = int(raw_input('Podaj liczbe: '))


def jestKwadratem(n):
    jest = False
    y = 1
    while (y < math.sqrt(n) + 1) and not jest:
        if (y * y) == n:
            jest = True
        y += 1
    return jest


lista = range(100000, 200000)

print len([val for val in map(jestKwadratem, lista) if val])
