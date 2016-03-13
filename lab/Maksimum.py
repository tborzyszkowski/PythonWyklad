
def max1(a, b):
    return a if a > b else b


def max2(*args, **kwargs):
    result = 0
    if args:
        result = reduce(max1, args)
        if kwargs:
            result = reduce(max1, [result] + kwargs.values())
    else:
        result = reduce(max1, kwargs.values())
    return result

print max2("Ala", "ma", "kota")
print max2(1, 2, 3, 4.5)
print max2(1, 2, 3, 4.5, x=8, y=9)
print max2(a=-1, b=-2)
kk = (1, 2, 3, 4, 5)
dd = {'x': 9, 'y': 8}
print max2(*kk, **dd)

# print max2(*("Ala ma kota".split()))
# a = "Ala \t ma    kota   "
# print a
# print a.split()
# print " ".join(a.split())
