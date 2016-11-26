# -*- coding: utf-8 -*-

d1 = 26
m1 = 11
r1 = 2016
d2 = 27
m2 = 11
r2 = 2016

if r2 > r1:
    print 'Data 2 większa niż Data 1'
elif r2 < r1:
    print 'Data 1 większa niż Data 2'
elif m2 > m1:
    print 'Data 2 większa niż Data 1'
elif m2 < m1:
    print 'Data 1 większa niż Data 2'
elif d2 > d1:
    print 'Data 2 większa niż Data 1'
elif d2 < d1:
    print 'Data 1 większa niż Data 1'
else:
    print 'Daty są sobie równe'

dd1 = (r1, m1, d1)
dd2 = (r2, m2, d2)

if dd1 < dd2:
    print "Pierwsza"
elif dd1 > dd2:
    print "Druga"
else:
    print "Rowne"

dl1 = r1 * 10000 + m1 * 100 + d1
dl2 = r2 * 10000 + m2 * 100 + d2

print dl1, dl2, "Pierwsza" if dl1 < dl2 else ("Druga" if dl1 > dl2 else "Rowne")
