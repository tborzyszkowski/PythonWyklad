# proste dziedziczenie


class A:
    def __init__(self, a=1):
        self.a = a

    def m(self):
        return self.a

    def test(self, a):
        print self.m() + a


class B(A):
    def __init__(self, a=2, b=3):
        # A.__init__(self)
        A.__init__(self, a)  # trzeba wywolac inicjalizacje przodka
        self.b = b

    def m(self):
        return self.a + self.b

    # def superM(self):
    #     return super


# teraz wywolamy

a = A()
print a.m()
a.test(2)

b = B()
print b.m()
b.test(3)
# print b.superM()
