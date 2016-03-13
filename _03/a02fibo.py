# liczby Fibonacciego


def fib(n):
    """Wypisuje liczby Fibonacciego mniejsze niz n
    """
    a, b = 0, 1
    while b < n:
        print b,
        a, b = b, a+b


def fib2(n):
    """Zwraca liste liczb Fibonacciego mniejszych niz n
    """
    result = []
    a, b = 0, 1
    while b < n:
        result.append(b)
        a, b = b, a+b
    return result


def silnia(n):
    if n == 0:
        return 1
    elif n > 0:
        return n * silnia(n-1)
    else:
        return (-1)*silnia((-1)*n)


def a(n):
    return n


def b(n):
    return a(n)
