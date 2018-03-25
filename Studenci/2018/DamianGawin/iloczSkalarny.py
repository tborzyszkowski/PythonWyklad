vec1 = [1, 2, 3, 4]
vec2 = [5, 6, 7, 8]


def skalar(vec1, vec2):
    wynik = [vec1[i] * vec2[i] for i in range(len(vec1))]
    return wynik


print (skalar(vec1, vec2))


def suma(list):
    for i in list:
        suma =+ i
    return suma


wynik = suma(skalar(vec1, vec2))

print (wynik)



