class A:
    def m(self):
        return 1

    def test(self):
        return self.m()

    def testSelf(self):
        return self.test()


class B(A):

    def m(self):
        return 2

    def testSuper(self):
        return A.test(self)


class C(B):

    def m(self):
        return 3

    def testSuper(self):
        return B.m(self)

a = A()
b = B()
c = C()
print 'A:', a.test(), a.testSelf()
print 'B:', b.test(), b.testSuper(), b.testSelf()
print 'C:', c.test(), c.testSuper(), c.testSelf()
