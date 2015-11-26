# proste dziedziczenie


class A:
    def __init__(self, a=1):
        self.a = a

    def m(self):
        return self.a

    def test(self):
        print self.m()


class B(A):
    def __init__(self, a=2, b=3):
        A.__init__(self, a)  # trzeba wywolac inicjalizacje przodka
        self.b = b

    def m(self):
        return self.a + self.b


# teraz wywolamy
B().test()
a = A()
print a.m()  # A.m(a)
