from random import randint

n = 5
daty = [{'dzien': randint(1, 28), 'miesiac': randint(1, 12), 'rok': randint(2000, 2021)} for i in range(n)]

print(len(daty))
for data in daty:
    print(data)


def czy_zamienic(data_pierwsza, data_druga):
    result = False
    if data_pierwsza['rok'] > data_druga['rok']:
        result = True
    elif data_pierwsza['rok'] == data_druga['rok']:
        if data_pierwsza['miesiac'] > data_druga['miesiac']:
            result = True
        elif data_pierwsza['miesiac'] == data_druga['miesiac']:
            if data_pierwsza['dzien'] > data_druga['dzien']:
                result = True
    return result


for i in range(n-1):
    data_1 = daty[i]
    for j in range(i+1, n):
        data_2 = daty[j]
        if czy_zamienic(data_1, data_2):
            daty[i], daty[j] = daty[j], daty[i]

print('-----------------')
for data in daty:
    print(data)

# sort = []
# x = 0
# for x in range(n):
#     daty['dzien'][x] = random.randint(1, 30)
#     daty['miesiac'][x] = random.randint(1, 12)
#     daty['rok'][x] = random.randint(2000, 2021)
#
#     y = ((daty['rok'][x] * 10000) + (daty['miesiac'][x] * 100) + daty['dzien'][x])
#     sort.append(y)
# x = 1
# for x in range(n):
#     y = sort[x]
#     i = 0
#     for i in range(x):
#         if sort[x] < sort[i]:
#             przech = sort[i]
#             sort[i] = sort[x]
#             sort[x] = przech
#
# x = 0
# for x in range(n):
#     print(sort[x] % 100, int((sort[x] % 10000 - (sort[x] % 100)) / 100), int((sort[x] - (sort[x] % 10000)) / 10000))