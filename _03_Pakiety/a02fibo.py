
def fib_rek(n):
    if n == 0 or n == 1:
        return n
    else:
        return fib_rek(n - 1) + fib_rek(n - 2)


def fib(n):
    """Wypisuje liczby Fibonacciego mniejsze niz n
    """
    a, b = 0, 1
    while b < n:
        print(b,)
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


def aa(n):
    return n


def bb(n):
    return aa(n)
