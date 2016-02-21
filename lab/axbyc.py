'''
ax + by + c =0
'''
a = 1
b = 0
c = 1
a
x = ((a == 0) and [(c == 0 and ['duzo'] or ['nie ma'])[0]] or [-c/float(a)])[0]
y = ('duzo' if c == 0 else 'nie ma') if a == 0 else -c/float(a)
print x, y

wynik = ""
if a ==0:
    if c == 0:
        wynik = 'duzo'
    else:
        wynik = 'nie ma'
else:
    wynik = -c/float(a)

print wynik
