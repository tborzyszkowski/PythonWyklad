# proste dziedziczenie


class A:
    def __init__(self, a = 1):
        self.a = a
    def m(self):
        return self.a
    def test(self, a_value):
        print(self.m() + a_value)


class B(A):
    def __init__(self, a = 2, b = 3):
        # A.__init__(self)
        A.__init__(self, a)  # trzeba wywolac inicjalizacje przodka
        self.b = b
    def m(self):
        return self.a + self.b
    def super_m(self):
        # return super
        return A.m(self)


a = A()
print(a.m())
a.test(2)

b = B()
print(b.m())
b.test(3)
print(b.super_m())
