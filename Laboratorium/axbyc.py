'''
ax + by + c =0
'''
# a = 1
# b = 1
# c = 0
przypadki = [(1, 0, 0), (1, 0, 1), (0, 1, 0), (0, 1, 1), (1, 1, 0), (1, 1, 1), (0, 0, 1)]

for (a, b, c) in przypadki:
    res = ('duzo' if c == 0 else 'nie ma') if a == 0 else -c/float(a)
    print a, "x +", b, "y + ", c, "=", 0, "res =", res

# print res

# x = ((a == 0) and [(c == 0 and ['duzo'] or ['nie ma'])[0]] or [-c/float(a)])[0]
# <warunek> ? wy1 : wyr2
# wyr1 if <warunek> else wyr2
# print x, y
#
# wynik = ""
# if a == 0:
#     if c == 0:
#         wynik = 'duzo'
#     else:
#         wynik = 'nie ma'
# else:
#     wynik = -c/float(a)
#
# print wynik
