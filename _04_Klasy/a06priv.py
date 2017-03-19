# atrybuty prywatne

# prywatna zmienna modulu
__b = 13

print '__b = ', __b

# przywatna funkcja


def __prywatna_funkcja(a=1):
    print 'Wewnatrz prywatnej funkcji, a = ', a

__prywatna_funkcja(7)
# prywatne atrybuty klasy


class Prywatna:
    def __init__(self):
        self.a = 10
        self.__b = 17

    def __f(self):
        print self.a, '  ', self.__b
        return 0

p = Prywatna()
print p.a
# print p.__b
print p._Prywatna__b
# print p.f()
print "--", dir(p)
