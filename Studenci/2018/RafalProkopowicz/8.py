# # zad3
#
# liczba = raw_input("liczba: ")
# length = len(str(liczba))
# y = []
# name = ("zero", "jeden", "dwa", "trzy", "cztery", "piec", "szesc", "siedem", "osiem", "dziewiec")
#
# for i in range(0, length):
#     y.append(name[int(str(liczba)[i])])
# print y


# ============================= #
# zad4

produkty = {
    "chleb": 12,
    "jajko": 4,
    "maslo": 2
}

def lista(produktname, ilosc):
    item = {produktname: produkty[produktname] * ilosc}
    return item

koszyk = []


# kupowanie
koszyk.append(lista("chleb", 3))
koszyk.append(lista("jajko", 16))
koszyk.append(lista("maslo", 5))

for x in range(0, koszyk.__len__()):
    print koszyk[x]

# ========================================== #
# zad5
# def returnmax(list):
#     listmax = list[0]
#     for x in range(0,list.__len__()):
#         if list[x] > listmax:
#             listmax = list[x]
#     return listmax
#
#
# tab = [1,4,5,2,100,5,7,3,2,0]
#
# print returnmax(tab)
#
#
#
