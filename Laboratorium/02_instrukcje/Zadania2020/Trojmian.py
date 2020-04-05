

def pierwiaski_trojmianu(a, b, c):
    """
    Wylicza pierwastki rownania kwadratowego

    :param a: wsplczynnik przy x ** 2
    :param b: wsplczynnik przy x
    :param c: wsplczynnik bez x
    :return:  { ile_pierwiastkow: n, pierwiastki: (0, ..., n-1) }
    """
    return {"ile_pierwiastkow": 0, "pierwiastki": (0,)}


print pierwiaski_trojmianu(1, 0, 1)