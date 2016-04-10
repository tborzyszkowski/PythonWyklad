import pickle

# print dir(pickle)

# x = 1 + 2j
# print 'x = ', x
# s = pickle.dumps(x)
# print 's = ', s
# y = pickle.loads(s)
# print 'y = ', y, x is y, x == y

# # Bardziej skomplikowany przyklad


class A:
    def __init__(self, a=1):
        self.a = a

    def m(self):
        return self.a

    def test(self):
        print self.m()


class B(A):
    def __init__(self, a=2, b=3):
        A.__init__(self, a)  # trzeba wywolac inicjalizacje przodka
        self.b = b

    def m(self):
        return self.a + self.b

    def __repr__(self):
        return ""+str(self.a)+", "+str(self.b)

a = A(11)
b = B(22, 33)
# print '='*20
# print pickle.dumps(A)
# print '-'*20
# print pickle.dumps(a)
# print '='*20
# print pickle.dumps(B)
# print '-'*20
# print pickle.dumps(b)
# print '='*20

# print pickle.loads(pickle.dumps(b))


lista = [1, "Ala", 1+2j, [1, 2]]
# print pickle.dumps(lista)
ll = pickle.loads(pickle.dumps(lista))
print 'll = ', ll, ll is lista, ll == lista
