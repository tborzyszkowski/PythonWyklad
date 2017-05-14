import math
import time

# x = int(raw_input('Podaj liczbe: '))


def jestPierwsza(n):
    jest = True
    y = 2
    straznik = math.sqrt(n)
    while (y <= straznik) and jest:
        if n % y == 0:
            jest = False
        y += 1
    return jest


lista = range(1000 * 1000, 2 * 1000 * 1000)

# print map(jestPierwsza, lista)
start_time = time.clock()
wynik = [val for val in map(jestPierwsza, lista) if val]
stop_time = time.clock()
print "Time:", stop_time - start_time, "Wynik:", len(wynik)


def sitoErastotenesa(n, k):
    lista = range(n, k+1)
    for i in range(2, int(math.sqrt(k))+1):
        pom = [val for val in lista if (val <= i) or (val % i != 0)]
        lista = pom
    return lista


start_time = time.clock()
wynik = sitoErastotenesa(1000 * 1000, 2 * 1000 * 1000)
stop_time = time.clock()
print "Time:", stop_time - start_time, "Wynik:", len(wynik)
