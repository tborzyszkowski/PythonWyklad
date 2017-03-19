# zmienne

print '----------'

# print zmienna
zmienna = 1
print zmienna, type(zmienna)

zmienna = 'Ala'
print zmienna, type(zmienna)

x, y, z = 1, 2, 3
print x, y, z
x, y, z = y, z, x
print x, y, z

# przypisanie zmiennym tej samej wartosci
x = y = z = (1,)
print x, y, z
x = (1,)
print x is y, y is z

# a co przypisze instrukcja
x = (y, z) = ([a], [b, c]) = ([1], [2, 3])
print x, y, z, a, b, c

# numerowanie
(pon, wt, sr, czw, pt) = range(5)
print pon, wt, sr, czw, pt
(pon, wt, sr, czw, pt) = range(1, 10, 2)
print pon, wt, sr, czw, pt
