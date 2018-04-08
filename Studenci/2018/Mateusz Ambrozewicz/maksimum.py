def maksimum(*dane):
    wynik = 0
    wynik = reduce((lambda x,y: max(x,y)),dane)
    return wynik

print maksimum('c', 'f', '3', 'x')
