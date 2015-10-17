
x = int(raw_input('Podaj liczbe: '))
jest = False
y = 1
while (y < x) and not jest:
    if (y * y) == x:
        jest = True
    y += 1

if jest:
    print 'TAK'
else:
    print 'NIE'