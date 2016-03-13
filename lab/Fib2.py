
def mult(m1, m2):
    n = len(m1)
    tmp = [[0 for i in range(n)] for j in range(n)]
    val = 0
    for i in range(n):
        for j in range(n):
            for c in range(n):
                val += m1[i][c] * m2[c][j]
            tmp[i][j] = val
            val = 0
    return tmp


def najwiekszaPotega2(n):
    i = 0
    za_duzo = False
    while not za_duzo:
        if 2**i > n:
            za_duzo = True
        else:
            i += 1
    return i-1


def listaPoteg2(n):
    if n == 1:
        return [0]
    else:
        k = najwiekszaPotega2(n)
        wyn = [k]
        if n == 2 ** k:
            return wyn
        else:
            wyn.extend(listaPoteg2(n-2**k))
            return wyn

# print listaPoteg2(9)


def multPow2(a, n):
    while n > 0:
        a = mult(a, a)
        n -= 1
    return a


def fib3(n):
    a = [[1, 1], [1, 0]]
    lista_macierzy = []

    for p in listaPoteg2(n):
        lista_macierzy.append(multPow2(a, p))

    return reduce(mult, lista_macierzy)[0][1]
