miesiace = {'luty': 28, 'maj': 31, 'lipiec': 31, 'wrzesien': 55, 'listopad': 20}

c = 1
for m in miesiace:
    miesiace[m] = c
    c += 1

print miesiace

miesiace = {k: miesiace.keys().index(k) + 1 for k in miesiace}

print miesiace
