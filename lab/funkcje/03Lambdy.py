# f = (lambda x: x + 1)
# print f(1), (lambda x: x + 1)(3)

# print (lambda x, y: y)(lambda y: y)
# oraz
# print (lambda x: (lambda y: y))(lambda z: z) ("Ala ma kota")
# print ( lambda x, y: x(y) ) ((lambda y: 2 * y +1), 1)
# print (lambda x, y: x)((lambda y: y), 1)(5)

# def fff(x):
#     return x % 2 != 0 and x % 3 != 0
#
# print filter(fff, range(2, 25))
#
# ff = (lambda x: x % 2 != 0 and x % 3 != 0)
# print filter(ff, range(2, 25))

# def cube(x):
#     return x*x*x
#
# szescian = (lambda x: x * x * x)
#
# print map(cube, range(1, 11))
# print map(szescian, range(1, 11))

# seq = range(8)
#
# def add(x, y):
#     return x+y
#
# print map(add, seq, seq)
# print map((lambda x, y: x+y), seq, seq)
#
def add(x, y):
    return x+y

print reduce(add, range(1, 11))
