'''
a * x**2 + b * x + c = 0
'''
from math import sqrt
a = 1
b = 0
c = 1
d = b * b - 4 * a * c

# wynik = ((a == 0) and [
#                         ((b == 0) and [ ((c == 0) and ['Dozo'] or ['Brak'])[0]
#                                       ] or
#                                      [ 'x = %f' % (-c)/(b*1.0)
#                                       ])[0]
#                         ] or
#                         [ ((d>0) and ['x1 = %f, x2 = %f' % ( (-b - sqrt(d))/(2*a), (-b + sqrt(d))/(2*a) )]
#                                 or  [ ((d==0) and ['x = %f' % ((-b)/(2.0*a))] or ["...."])[0] ]) [0]
#                          ]
#          )[0]
#
# print wynik
#
# wynik = (('Duzo' if (c == 0) else 'Brak')
#             if (b == 0) else 'x = %f' % (-c)/(b*1.0)) \
#         if (a == 0) \
#         else 'x1 = %f, x2 = %f' % ((-b - sqrt(d))/(2*a), (-b + sqrt(d))/(2*a)) \
#         if (d > 0) else \
#         ('x = %f' % ((-b)/(2.0*a)) if (d == 0) else "....")
# print wynik

if a == 0:
    if b ==0:
        if c==0:
            print 'Duzo'
        else:
            print "Brak"
    else:
        print 'x = ', (-c)/(b*1.0)
else:
    d = b * b - 4 * a * c
    if d > 0:
        dd = sqrt(d)
        print 'x1 = ', (-b - dd)/(2*a)
        print 'x2 = ', (-b + dd)/(2*a)
    elif d == 0:
        print 'x = ', (-b)/(2.0*a)
    else:
        dd = sqrt(-d)*1j
        print 'x1 = ', (-b - dd)/(2*a)
        print 'x2 = ', (-b + dd)/(2*a)
