
tt = (lambda x, y: x)
ff = (lambda x, y: y)
jesli = (lambda b, x, y: b (x, y) )

jesli (tt, 1, 2)
jesli (ff, 1, 2)

para = (lambda x, y: (lambda b: jesli (b, x, y)))
fst = (lambda p: p(tt))
snd = (lambda p: p(ff))

print fst (para (1,2))
print snd (para (1,2))

zero = (lambda f, x: x)
succ = (lambda n: (lambda f, x: f(n (f, x))))
jeden = succ (zero)
dwa = succ (jeden)
trzy = succ(dwa)

f = (lambda x: x + 1)
zz = 0

print zero (f, zz)
print jeden (f, zz)
print dwa (f, zz)
print trzy (f, zz)

