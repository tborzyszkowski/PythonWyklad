class A:
    i = 2
    def __init__(self, a=10):
        self.a = a+1
    def f(self):
        return 2*self.a

class B(A):
    j = 1
    def __init__(self, b=9):
        A.__init__(self, 8)
        self.__class__.i += 1
        self.b = b
    def f(self):
        return self.b + self.a
    def g(self):
        return self.__class__.i + self.__class__.j + self.f()


class C(B):
    def __init__(self, c=10):
        B.__init__(self)
        self.c = c
    def f(self):
        return B.f(self) * self.c

c = C()
print 'a = ', c.a, 'b = ', c.b, 'c = ', c.c
print 'i = ', c.__class__.i, 'j = ', c.__class__.j
print 'c.f() = ', c.f(), 'c.g() = ', c.g()