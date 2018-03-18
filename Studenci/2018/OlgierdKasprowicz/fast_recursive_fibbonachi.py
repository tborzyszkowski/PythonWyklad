#!/usr/bin/env python3

"""
This is a benchmark utility
See more at: https://stackoverflow.com/a/41408510
"""

from timeit import default_timer as timer

class benchmark(object):

    def __init__(self, msg, fmt="%0.3g"):
        self.msg = msg
        self.fmt = fmt

    def __enter__(self):
        self.start = timer()
        return self

    def __exit__(self, *args):
        t = timer() - self.start
        print(("%s : " + self.fmt + " seconds") % (self.msg, t))
        self.time = t

from functools import lru_cache


def fib(n):
    if n == 0:
        return 0
    if n == 1:
        return 1

    return fib(n-1) + fib(n-2)


@lru_cache(maxsize=3)
def fast_fib_recursive(n):
    if n == 0:
        return 0
    if n == 1:
        return 1

    return fast_fib_recursive(n-1) + fast_fib_recursive(n-2)


def main():
    with benchmark("Naive fib(30)"):
        print(fib(35))
    with benchmark("Memoised fib(30)"):
        print(fast_fib_recursive(35))


if __name__ == "__main__":
    main()
