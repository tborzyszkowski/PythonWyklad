przypadki = [(1, 1), (2, 1), (3, 3), (4, 1), (5, 3), (6, 5), (7, 7), (8, 1), (9, 3), (10, 5), (11, 7), (12, 9), (13, 11), (14, 13)]
for (liczbaRycerzy, wynik) in przypadki:
    listaRycerzy = [x for x in range(liczbaRycerzy)]

    i = 1
    while len(listaRycerzy) > 1:
        del listaRycerzy[i]
        i += 1
        i %= len(listaRycerzy)
    print "Rycerze:", liczbaRycerzy, "\tActual:", listaRycerzy[0] + 1, "\tExpected:", wynik, listaRycerzy[0] + 1 == wynik
