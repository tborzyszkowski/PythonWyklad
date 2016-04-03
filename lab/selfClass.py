class SelfTest:
    i = 5

    def __init__(self, arg):
        self.i = arg


st1 = SelfTest(7)
st2 = SelfTest(-7)
st1.__class__.i = 0
print st1.i, st1.__class__.i
print st2.i, st2.__class__.i
