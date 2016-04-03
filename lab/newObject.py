class FooOld:
    i = 0


class FooNew(object):
    i = 0


print type(FooOld())
print type(FooNew())

# MRO: Method Resolution Order
# L[C(B1 ... BN)] = C + merge(L[B1] ... L[BN], B1 ... BN)


class FooOld1(FooOld):
    pass


class FooOld2(FooOld):
    i = 2


class FooOld12(FooOld1, FooOld2):
    pass

class FooOld21(FooOld2, FooOld1):
    pass

print FooOld12().i, FooOld21().i
