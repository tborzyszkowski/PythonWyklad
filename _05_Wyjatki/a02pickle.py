import pickle

print(dir(pickle))

x = 1 + 2j
print('x = ', x)
s = pickle.dumps(x)
print('s = ', s)
y = pickle.loads(s)
print('x = ', x, 'y = ', y, x is y, x == y)

y += 1
print('x = ', x, 'y = ', y, x is y, x == y)


# Bardziej skomplikowany przyklad


# class A:
#     def __init__(self, a=1):
#         self.a = a
#     def __repr__(self):
#         return "A:[ a = "+str(self.a) + " ]"
#
#
# class B(A):
#     def __init__(self, a=2, b=3):
#         A.__init__(self, a)  # trzeba wywolac inicjalizacje przodka
#         self.b = b
#     def __repr__(self):
#         return "B:[ a = "+str(self.a)+", b = "+str(self.b) + " ]"
#
# a = A(11)
# b = B(22, 33)
# print a
# print b
#
# a = A(11)
# b = B(a, 33)
# print a
# print b
#
# bDeep = pickle.dumps(b)
# bb = pickle.loads(bDeep)
# print bb
#
# bb.a.a = -999
# print bb
# print b
# print '='*20
# print pickle.dumps(A)
# print '-'*20
# print pickle.dumps(a)
# print '='*20
# print pickle.dumps(B)
# print '-'*20
# print pickle.dumps(b)
# print '='*20
#
# print pickle.loads(pickle.dumps(b))
#
#
# lista = [1, "Ala", 1+2j, [1, 2]]
# # print pickle.dumps(lista)
# ll = pickle.loads(pickle.dumps(lista))
# print 'll = ', ll, ll is lista, ll == lista
#
#
# class Maz:
#     def __init__(self, zona=1):
#         self.bylem = False
#         self.zona = zona
#     def __repr__(self):
#         s = ""
#         if not self.bylem:
#             self.bylem = True
#             s = "Maz:[ zona = "+str(self.zona) + " ]"
#         else:
#             s = "..."
#         self.bylem = False
#         return s
#
#
# class Zona:
#     def __init__(self, maz=1):
#         self.bylem = False
#         self.maz = maz
#     def __repr__(self):
#         s = ""
#         if not self.bylem:
#             self.bylem = True
#             s = "Zona:[ maz = "+str(self.maz) + " ]"
#         else:
#             s = "..."
#         self.bylem = False
#         return s
# m = Maz()
# z = Zona(m)
# m.zona = z
#
# mm = pickle.dumps(m)
#
# print m is mm, mm == m
# print m
# x = [1]
# y = [x, 0]
# y[1] = y
# print y

# m.deepcopy()