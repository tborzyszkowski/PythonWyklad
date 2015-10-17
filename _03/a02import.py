import a02fibo

a02fibo.fib(1000)
print
print a02fibo.fib2(1000)

print "-"*20

from a02fibo import fib, fib2

fib(2000)
print
print fib2(2000)


print "="*20

a = 5

import a01nazwa

print a
print a01nazwa.a

from a01nazwa import a

print a
a = 3
print a
print a01nazwa.a

