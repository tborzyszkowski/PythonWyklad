# if, for, while

# --- prosty test
# x = 20 #int(input('Podaj liczbe od 1 do 10: '))
# if x < 0:
#     print('Tylko tyle?')
# elif 0 <= x <= 10:
#     print('OK')
# else:
#     print('Za duzo')

# # --- iteracja
# a = ['Ala', 'ma', 'kota', (1, 2, 3)]
# for x in a:
#     print(x, len(x))
#     # a.append([1])

# # --- co to?
# x = 997 * 997 #int(input('Podaj liczbe: '))
# jest = True
# y = 2
# while (y < x) and jest:
#     if (x % y) == 0:
#         jest = False
#     y += 1
#
# if jest:
#     print('TAK')
# else:
#     print('NIE')

# # --- petla z else
#
# for x in range(0, 20, 3):
#     print(x)
# else:
#     print('KONIEC', x)
#
# print(globals())
# if True:
#     x = 5
#     print(globals())
# print(x)
# print(globals())

n = 10000
licznik = 1
wynik = 1
while licznik <= n:
    wynik *= licznik
    licznik += 1
else:
    print(wynik)