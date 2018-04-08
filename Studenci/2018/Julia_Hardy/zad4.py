def spis(x,y):
    lista_towarow = {}
    for i in y:
        if i in x:
            if x[i][1]< y[i]:
                print 'w sklepie nie ma tyle %s mozesz kupic tylko %d' %(i,x[i][1])
                lista_towarow[i] = x[i][0]*x[i][1]
            else:
                lista_towarow[i] = x[i][0]*y[i]
        else:
            print'w sklepie nie ma %s' %(i)
    return lista_towarow

towary= {'woda': [2.5, 16], 'jabko': [1.5, 25] }
zamowienie= {'woda':25, 'kurczak':13, 'jabko':5}

print spis(towary,zamowienie)
