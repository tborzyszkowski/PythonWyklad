import a02fibo
from a02fibo import fib, fib2, silnia, bb


def run_a01nazwa():
    import a01nazwa
    global a
    print(a01nazwa.a)
    # del a01nazwa
    print(a)
    print(a01nazwa.a)
    from a01nazwa import a
    print(a)
    a = 3
    # from a02fibo import a
    print(a)
    print(a01nazwa.a)


if __name__ == '__main__':
    a02fibo.bb(4);
    bb(7)
    print(a02fibo.fib(100000))
    print()
    print(a02fibo.fib2(100000))

    print(fib(200000))
    print(fib2(200000))
    print(silnia(4))
    print(silnia(-4))
    a = 5

    run_a01nazwa()
