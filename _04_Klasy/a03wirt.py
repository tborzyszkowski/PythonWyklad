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
    print('B:', b.test(), b.test_super(), b.test_self()) # 2 2 2 |
    print('C:', c.test(), c.test_super(), c.test_self()) # 3 2 3

# b.test() = B.test(b) = A.test(b) = b.m() = B.m(b) = 2
# b.test_super() = B.test_super(b) = A.test(b) = b.m() = B.m(b) = 2
# c.test() = A.test(c) = c.m() = C.m(c) = 3
# c.test_super() = C.test_super(c) = B.m(c) = 2
# c.test_self() = A.test_self(c) = c.test() = 3
