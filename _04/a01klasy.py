# proste definicje klas


class NicNieRob:
    pass

# print dir(NicNieRob)

# przykladowa klasa bez inicjalizacji


class MyClass:
    """A simple example class.
    """
    i = 12345

    def f(self):
        """Opis funkcji
        """
        return 'hello world %d' % self.__class__.i

x = MyClass()
y = MyClass()
# print x.f()
# print x.__class__.i, y.__class__.i
# y.i = 54321
# # y.__class__.i = 13579
# print x.__class__.i, y.__class__.i
# print x.f(), y.f()
# print y.i, x.i


# print x.__doc__
# print x.f.__doc__
# print '-'*20
#
# # klasa z inicjalizacja stanu klasy

class MojaKlasa:
    i = 0

    def __init__(self, a=10, b=20):
        self.__class__.i += 1
        self.a = a
        self.b = b

    def wypisz(self):
        print self.i, self.a, self.b


y = MojaKlasa(30, 40)
y.wypisz()
z = MojaKlasa()
z.wypisz()
y.wypisz()
MojaKlasa(13).wypisz()
z.wypisz()
y.wypisz()

# y.wypisz()

# # czym jest
# print MojaKlasa.wypisz
# # a czym
# print y.wypisz
#
# # z drugiej strony
# y.wypisz()
# # jest rownowazne
# MojaKlasa.wypisz(z)
# nn = NicNieRob()
# nn.i = 0
# nn.a = 2
# nn.b = 3
# MojaKlasa.wypisz(nn)
#
#
# kasujemy atrybuty obiektu
# del y.i
# del y.__class__.i
del y.a
# print y.a
print z.a

#
# # a teraz klasy
del MojaKlasa.i
# # metody tez mozemy kasowac
del MojaKlasa.wypisz
# # ale czy z obiektu tez mozna usuwac metody?
