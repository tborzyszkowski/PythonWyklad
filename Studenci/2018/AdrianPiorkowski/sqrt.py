n=int(raw_input("podaj liczbe"))
i=n/2
d=n
while d!=0:
    if i*i==n:
        print i
        break
    elif i*i>n:
        d=d/2
        i=i-d
    else:
        d = d / 2
        i =i+ d
else:
    print "brak"