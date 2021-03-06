# if, for, while

# --- prosty test
x = int(input('Podaj liczbe od 1 do 10: '))
if x < 0:
    print('Tylko tyle?')
elif 0 <= x <= 10:
    print('OK')
else:
    print('Za duzo')

# --- iteracja
a = ['Ala', 'ma', 'kota']
for x in a:
    print(x, len(x))

# --- co to?
x = int(input('Podaj liczbe: '))
jest = True
y = 2
while (y < x) and jest:
    if (x % y) == 0:
        jest = False
    y += 1

if jest:
    print('TAK')
else:
    print('NIE')

# --- petla z else

for x in range(0, 20, 3):
    print(x)
else:
    print('KONIEC')

n = 5
x = 1
w = 1
while x < n:
    x += 1
    w *= x
else:
    print(w)
