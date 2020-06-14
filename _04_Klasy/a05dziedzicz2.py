# przyklady dziedziczenia wielokrotnego


class A:
    i = 1

    def __init__(self, a=10):
        self.a = a

    def f(self):
        return self.a

    def getI(self):
        return self.__class__.i

    def h(self):
        return self.f() + self.getI()


class B1(A):
    j = -1

    def __init__(self):
        A.__init__(self, 101)
        self.__class__.i += 1
        self.b = 110

    def f(self):
        return self.b - self.a

    def getI(self):
        return self.__class__.i + self.__class__.j


class B2(A):
    j = -2

    def __init__(self):
        A.__init__(self, 21)
        self.__class__.i += 2
        self.b = 11

    def f(self):
        return self.a * self.b

    def getI(self):
        return self.__class__.i - self.__class__.j


class C(B1, B2):
    def __init__(self):
        B1.__init__(self)
        B2.__init__(self)


c = C()
print 'a = ', c.a, ' b = ', c.b, ' i = ', c.__class__.i, ' j = ', c.__class__.j
print 'c.f() = ', c.f(), ' c.getI() = ', c.getI(), 'c.h() = ', c.h()
