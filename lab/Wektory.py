
w1 = (1,2,3)
w2 = (4,5,6)

def skalar(a, b):
    s = 0
    for i in range(0, len(a)):
        s += a[i]*b[i]
    return s

print skalar(w1, w2)

# reduce((lambda x, y: x + y), [1, 2, 3, 4]) == 1 + 2 + 3 + 4
def skalar2(a, b):
    return reduce((lambda x, y: x + y), [a[i]*b[i] for i in range(0,len(a))])
 
print skalar2(w1,w2)    