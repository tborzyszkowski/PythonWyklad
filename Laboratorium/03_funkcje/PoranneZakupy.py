oferta = {'chleb': 2.5, 'mleko': 1.99, 'wiejski': 4.15, 'platki': 10}

portfel = 100


def zakupy(oferta, portfel, **listaZakupow):
    kupno = {k: 0 for k in listaZakupow}
    for k in listaZakupow:
        if k in oferta:
            kupno[k] = listaZakupow[k] * oferta[k]
    suma = 0
    for p in kupno:
        suma += kupno[p]
    return (kupno, portfel - suma)


# print zakupy(oferta, portfel, chleb=2, mleko=3, wiejski=1, mlotek=3)

dd = {"chleb": 2, "mleko": 3, "wiejski": 1, "mlotek": 3}
print zakupy(oferta, portfel, **dd)