class FooOld:
    i = 0


class FooNew(object):
    i = 0


print type(FooOld())
print type(FooNew())

# MRO: Method Resolution Order
# L[C(B1 ... BN)] = C + merge(L[B1] ... L[BN], B1 ... BN)

# old class test


class FooOld1(FooOld):
    pass


class FooOld2(FooOld):
    i = 2


class FooOld12(FooOld1, FooOld2):
    pass


class FooOld21(FooOld2, FooOld1):
    pass


print FooOld12().i, FooOld21().i

# new class test


class FooNew1(FooNew):
    pass


class FooNew2(FooNew):
    i = 2


class FooNew12(FooNew1, FooNew2):
    pass


class FooNew21(FooNew2, FooNew1):
    pass


print FooNew12().i, FooNew21().i

#
