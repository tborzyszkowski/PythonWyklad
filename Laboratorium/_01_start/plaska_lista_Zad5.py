lista = [[1, 2, 3], ["Abba", "aff"], [-2, 4, 5]]

result = []
for el in lista:
    for sub_el in el:
        result.append(sub_el)

print(result)