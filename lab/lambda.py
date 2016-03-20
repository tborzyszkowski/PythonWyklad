tt = (lambda x, y: x)
ff = (lambda x, y: y)
jesli = (lambda b, x, y: b(x, y))

# print tt(1, 2)
# print ff(1, 2)
# print jesli(tt, 1, 2)
# print jesli(ff, 1, 2)
# #
para = (lambda x, y: (lambda b: jesli(b, x, y)))
fst = (lambda p: p(tt))
snd = (lambda p: p(ff))

# print para(1, 2)(ff)
# print fst(para(1, 2))
# print snd(para(1, 2))

zero = (lambda f, x: x)
succ = (lambda n: (lambda f, x: f(n(f, x))))
jeden = succ(zero)
dwa = succ(jeden)
trzy = succ(dwa)

f = (lambda x: x * 2)
zz = 1

print zero(f, zz)
print jeden(f, zz)
print dwa(f, zz)
print trzy(f, zz)
#
# # Fixed-point combinator
# # https://en.wikipedia.org/wiki/Fixed-point_combinator
#
# # Z combinator

Z = lambda f: (lambda x: f(lambda *args: x(x)(*args)))(lambda x: f(lambda *args: x(x)(*args)))
add = Z(lambda f: lambda a, b: b if a <= 0 else 1 + f(a - 1, b))
print add(1, 1)
print add(100, 200)

# Y combinator

Y = lambda g: (lambda f: g(lambda arg: f(f)(arg)))(lambda f: g(lambda arg: f(f)(arg)))
factorial = Y(lambda f: (lambda num: num and num * f(num - 1) or 1))
print factorial(5)
