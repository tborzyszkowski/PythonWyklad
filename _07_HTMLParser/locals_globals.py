def f(arg):
    x = 1
    print(locals())


f(7)
f('aaa')

print(globals())
#
# # -------------------
# print 20*'-'
#


def g(arg):
    x = 1
    print(locals())
    locals()["x"] = 2
    print("x = ", x)


z = 7
print("z = ", z)
g(3)
globals()["z"] = 8
print("z = ", z)
#
