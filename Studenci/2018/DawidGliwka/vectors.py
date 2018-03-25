def getvector(v):
    c = input("Podaj wsp. wektora: ")
    while 1:
        v.append(int(c))
        c = raw_input("Podaj kolejna wsp. wektora: ")
        if c == "":
            break
    return v

v1 = []
v2 = []


def vecscalar(v1, v2):
    if len(v1) != len(v2):
        print "blad, wektory nie maja tych samych wymiarow"
    else:
        scalar = 0
        while v1:
            scalar += v1.pop(0) * v2.pop(0)
        return scalar

getvector(v1)
getvector(v2)
print vecscalar(v1, v2)
