class A:
    def m(self):
        return 1

    def test(self):
        return self.m()

    def test_self(self):
        return self.test()


class B(A):
    def m(self):
        return 2

    def test_super(self):
        return A.test(self)


class C(B):
    def m(self):
        return 3

    def test_super(self):
        return B.m(self)


if __name__ == "__main__":
    a = A()
    b = B()
    c = C()
    print('A:', a.test(), a.test_self())  # 1 1
    print('B:', b.test(), b.test_super(), b.test_self())
    print('C:', c.test(), c.test_super(), c.test_self())

# b.test() = B.test(b) = A.test(b) = b.m() = 2
# c.test() = A.test(c) = c.m() = C.m(c) = 3
# c.testSuper() = C.testSuper(c) = B.m(c) = 2
# c.testSelf() = A.testSelf(c) = c.test() = 3
