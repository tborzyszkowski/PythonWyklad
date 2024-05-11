__b = 13

def __prywatna_funkcja(a=1):
    print('Wewnatrz prywatnej funkcji, a = ', a)

# __prywatna_funkcja(7)
# prywatne atrybuty klasy


class Prywatna:
    def __init__(self):
        self.a = 10
        self.__b = 17

    def __f(self):
        print(self.a, '  ', self.__b)


if __name__ == "__main__":
    print(__b)
    p = Prywatna()
    print(p.a)
    # print(p.__b)
    print(p._Prywatna__b)
    # print p.__f()
    print(p._Prywatna__f())
    print("--", dir(p))
    print(p.__module__)
