from datetime import datetime
from functools import reduce


def silnia(n):
    result = 1
    for i in range(2, n+1):
        result = result * i
    return result


def silnia_rek(n):
    if n == 0:
        return 1
    else:
        return n * silnia_rek(n-1)


def silnia_reduce(n):
    return reduce((lambda x, y: x * y), range(1, n+1))


if __name__ == "__main__":
    n = 100 * 1000
    t1 = datetime.now()
    print(len(str(silnia(n))))
    # print(silnia(n))
    t2 = datetime.now()
    print("Bubble time:   ", (t2 - t1).total_seconds() * 1000)

    t1 = datetime.now()
    # print(len(str(silnia_rek(n))))
    print(len(str(silnia_reduce(n))))
    t2 = datetime.now()
    print("Bubble time:   ", (t2 - t1).total_seconds() * 1000)

