'''
Created on 2009-03-15

@author: tomek
'''
x = ''
y = 'yy'
print (1 and [x] or [y])[0]

print 1 and x or y

x = ['a', 'b', 'c', 'd', 'e', 'f']
print x[-5:-1]

#x = int(raw_input('Podaj liczbe: '))
x = 2999
jest = True
y = 2
while (y < x) and jest:
    if (x % y) == 0:
        jest = False
    y += 1

if jest:
    print 'TAK'
else:
    print 'NIE'

print 'abc' < 'bac' < 'cba', 'abc' < 'cba' < 'bca'

x = 1
y = 2
def f(a):
    global x
    x = a
    y = a + 1
    
f(4)
print x, y


def g(z, *a, **b):
    s = 0
    for k in b.keys():
        s = s + b[k]
    return s
        
print g(a = 3, z = 6, v = 9, w = 13)

x = [1, 2, 3, 4]
y = [4, 3, 2, 1]
print [a*b for a in x for b in y ]

print (0 and (lambda x:x+1) or (lambda x:x-1)) (0) 