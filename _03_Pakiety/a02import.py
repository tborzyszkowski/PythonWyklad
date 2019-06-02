import a02fibo

print a02fibo.fib(100000)
print
print a02fibo.fib2(100000)

print "-"*20

from a02fibo import fib, fib2, silnia

print fib(200000)
print
print fib2(200000)
print silnia(4)
print silnia(-4)

print "="*20

a = 5

import a01nazwa
print a01nazwa.a
# del a01nazwa
print a
print a01nazwa.a

from a01nazwa import a

print a
a = 3
# from a02fibo import a

print a
print a01nazwa.a
