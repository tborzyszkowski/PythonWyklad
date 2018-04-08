# Skladdnia listy towaru 'nazwa towaru' : [cena,ilosc]

ListaTowaru = {'chleb': [1.5,2], 'bulka': [0.75,11]}
ListaZakupow = {'bulka': 2, 'chleb': 3}

def zakupy(ListaZakupow, ListaTowaru):
    wynik = {}
    for k in ListaZakupow:
        for l in ListaTowaru:
            if k == l:
                if ListaTowaru[l][1] <= ListaZakupow[k]:
                    wynik[k] = (ListaZakupow[k] * ListaTowaru[l][0])
                else:
                    wynik[k] = 'Brak towaru'
    return wynik


print zakupy(ListaZakupow, ListaTowaru)
