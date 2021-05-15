class A(object):
    def __init__(self):
        super(A, self).__init__()
        print('init A')


class B(object):
    def __init__(self):
        super(B, self).__init__()
        print('init B')


class C(B, A):
    def __init__(self):
        super(C, self).__init__()
        print('init C')


c = C()
