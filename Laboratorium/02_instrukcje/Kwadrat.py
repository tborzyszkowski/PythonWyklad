import math

# x = int(raw_input('Podaj liczbe: '))


def jestKwadratemPom(n, l, p):
    if l <= p:
        y = l + (p - l) / 2
        if (y * y) > n:
            return jestKwadratemPom(n, l, y-1)
        elif (y * y) < n:
            return jestKwadratemPom(n, y+1, p)
        else:
            return True
    else:
        return False

def jestKwadratem(n):
    return jestKwadratemPom(n, 0 , n)

print jestKwadratem(0)
print jestKwadratem(1)
print jestKwadratem(2)
print jestKwadratem(3)
# lista = range(100000, 200000)
#
# print len([val for val in map(jestKwadratem, lista) if val])
