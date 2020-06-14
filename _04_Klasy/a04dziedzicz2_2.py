# przyklady dziedziczenia wielokrotnego


class B1:
    i = 1

    def __init__(self):
        self.a = 10
        self.b = 20
        self.i = 13

    def f(self):
        return self.a + self.b

    def getI(self):
        return self.i


class B2:
    i = -1

    def __init__(self):
        self.a = 100
        self.b = 200

    def f(self):
        return self.a * self.b

    def getI(self):
        return self.i


class C(B1, B2):

    def __init__(self):
        B1.__init__(self)
        B2.__init__(self)

    def g(self):
        return self.f()

    def h(self):
        return self.getI()


c = C()
c.__class__.i += 10
print 'a = ', c.a, ' b = ', c.b, ' class.i = ', c.__class__.i, 'self.i = ', c.i
print 'c.g() = ', c.g(), 'c.h() = ', c.h()
