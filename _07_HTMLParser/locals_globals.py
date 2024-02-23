def f(arg):
    x = 1
    print(locals())



def g(arg):
    x = 1
    print(locals())
    locals()["x"] = 2
    print("x = ", x)


z = 7

if __name__ == "__main__":
    # f(7)
    # f('aaa')
    # print(globals())
    print("z = ", z)
    g(3)
    globals()["z"] = 8
    print("z = ", z)

