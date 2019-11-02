class A:
    i = 3
    def __init__(self, a=20):
        self.a = a
    def f(self):
        return self.a

class B(A):
    j = -1
    def __init__(self, b=10):
        A.__init__(self, 10)
        self.__class__.i -= 1
        self.b = b
    def f(self):
        return self.b + self.a
    def g(self):
        return self.__class__.i + self.__class__.j + self.f()


class C(B):
    def __init__(self, c=20):
        B.__init__(self)
        self.c = c
    def f(self):
        return B.f(self) * self.c

c = C()
print 'a = ', c.a, 'b = ', c.b, 'c = ', c.c
print 'i = ', c.__class__.i, 'j = ', c.__class__.j
print 'c.f() = ', c.f(), 'c.g() = ', c.g()
