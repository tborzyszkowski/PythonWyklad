import random
import time
import math
import sys
from functools import reduce
from timeit import default_timer


def is_prime(num):
    for j in range(2, int(math.sqrt(num)) + 1):
        if (num % j) == 0:
            return False
    return True


def euklidesMod(a, b):
    if a <= b:
        return euklidesMod(b, a)
    elif b == 0:
        return a
    else:
        return euklidesMod(b, a % b)


def euklides(a, b):
    if a == 0 or b == 0:
        return -1
    a = -a if a < 0 else a
    b = -b if b < 0 else b
    while a != b:
        if a > b:
            a -= b
        else:
            b -= a
    return a

def euklides_multi(*args):
    return reduce(euklides, args)


if __name__ == '__main__':
    # print euklides(160, 120)


    # def euklides2(*args):
    #     return reduce(euklidesMod, args)

    # lista = [16, 4, 8]
    # print(euklides_multi(1,2,3,4))

    # print reduce(lambda x,y: x+y,[1,2,3])

    # print map(lambda x: x+1, [1])

    # if sys.platform == 'win32':
    #     # On Windows, the best timer is time.clock
    #     default_timer = time.clock
    # else:
    #     # On most other platforms the best timer is time.time
    #     default_timer = time.time



    big1 = random.getrandbits(256)
    big2 = random.getrandbits(256)
    fst = 10000000000
    snd = 10000010000

    start = default_timer()

    big3 = filter(is_prime, range(fst, snd))

    lista = [x for x in big3]
    stop = default_timer()
    print('Time is_prime:', stop - start)
    print(len(lista))

    prime = 0
    if big3:
        prime = lista[0]
    else:
        prime = 997
    print(prime)


    start = default_timer()
    lista = []
    for prime in big3:
        lista.append(
            (prime, euklidesMod(prime * prime, prime * prime * prime))
        )
    stop = default_timer()

    print('Time euklidesMod:', (stop - start))

    # start = default_timer()
    for prime in big3:
        print(euklides(prime * prime, prime * prime * prime))
    stop = default_timer()
    print('Time euklides:', stop - start)
