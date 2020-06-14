# przyklady dziedziczenia wielokrotnego


class B1:
    i = 1

    def __init__(self):
        self.a = 10
        self.b = 20
        self.c = 15

    def f(self):
        return self.a + self.b

    def getI(self):
        return self.__class__.i


class B2:
    i = -1

    def __init__(self):
        self.a = 100
        self.b = 200

    def f(self):
        return self.a * self.b

    # def getI(self):
    #     return self.__class__.i


class C(B2, B1):

    def __init__(self):
        B1.__init__(self)
        B2.__init__(self)

    def g(self):
        return self.f()

    def h(self):
        return self.getI()


c = C()
print 'a = ', c.a, ' b = ', c.b, ' i = ', c.__class__.i, ' c = ', c.c
print 'c.g() = ', c.g(), 'c.h() = ', c.h()
