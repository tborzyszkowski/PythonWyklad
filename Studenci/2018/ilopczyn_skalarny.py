def iloczyns(a=[2,1],b=[2,5]):
    c=0
    x=len(a)
    for i in range(1,x+1):
        iloczyn = a[i-1]*b[i-1]
        c+=iloczyn
    print c
    return

iloczyns([2,1,5],[2,6,6])
