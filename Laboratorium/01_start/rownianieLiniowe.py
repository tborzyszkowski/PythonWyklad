listaPrzypadkow = [(1, 1), (2, 3), (0, 0)]

for para in listaPrzypadkow:
    a = para[0]
    c = para[1]
    print "(a, c) = ", para
    if a == 0:
        if c == 0:
            print "nieskonczenie wiele"
        else:
            print "brak"
    else:
        print "Jedno:", (-1.0) * c / a