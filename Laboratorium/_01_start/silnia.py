def silnia(n):
    if n == 0:
        return 1
    else:
        return n * silnia(n-1)

def fib(n):
    if n < 2:
        return 1
    else:
        return fib(n-1) + fib(n-2)