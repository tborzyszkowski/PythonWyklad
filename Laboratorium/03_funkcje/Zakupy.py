
oferta = {'a': 1, 'b': 2, 'c': 3}
portfel = 100


def zakupy(l, p, *x):
    s = 0
    for k in x:
        s += l[k]

    return (s, p - s)

# def zakupy2(l, *x):
#     return reduce((lambda x, y: x+y), [l[k] for k in x])

print zakupy(oferta, portfel, 'a', 'c', 'c', 'a', 'b')
# aaa = ['a', 'b', 'c']
# print zakupy2(lista,*aaa)
