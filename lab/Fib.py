import time
from Fib2 import fib3


def fib2(n):
    f1 = 0
    f2 = 1
    k = n - 2
    if n < 2:
        f2 = n
    else:
        while k >= 0:
            f2, f1, k = f1 + f2, f2, k-1
    return f2


def fib(n):
    if n < 2:
        return n
    else:
        return fib(n-1) + fib(n-2)

n = 10

start_time = time.clock()
print fib(n)
print "Time fib: ", time.clock() - start_time, "sec"

start_time = time.clock()
print fib2(n)
print "Time fib2:", time.clock() - start_time, "sec"

start_time = time.clock()
print fib3(n)
print "Time fib2:", time.clock() - start_time, "sec"
# for (x, y) in [(1, 2), (3, 4)]:
#     print y
