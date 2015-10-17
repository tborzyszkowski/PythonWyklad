class A:
    def x(self):
        return 'a'

    def test(self):
        return self.x()

class B(A):
    def x(self):
        return 'b'

    def test(self):
        return A.test(self)

class C(B):
    def x(self):
        return 'c'
    
    def test(self):
        return B.x(self)

print A().test(), B().test(), C().test()