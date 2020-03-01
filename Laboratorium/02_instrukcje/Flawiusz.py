liczbaRycerzy = 5

# init
listaRycerzy = [x for x in range(liczbaRycerzy)]

i = 1
while len(listaRycerzy) > 1:
    del listaRycerzy[i]
    i += 1
    i %= len(listaRycerzy)
print listaRycerzy[0] + 1
