# operacje arytmetyczne na zwyklych liczbach calkowitych
# INT
# x = 3
# y = 2

# LONG
# x = 1000
# y = 400

# FLOAT
x = 3.333
y = 1.234

# COMPLEX
# x = 3+2j
# y = 2+1j

print(type(x))
result = x + y
print(x, " + ", y, " = ", result)
print(x - y)
print(x * y)
print(x / y)  # dzielenie calkowite
print(x // y)  # zaokraglenie w dol dzielenia calkowitego
# 3/0.7 3//0.7

print(x % y)  # reszta z dzielenia
print(-x)
print(+x)
print(abs(x))  # wartosc bezwzgledna
# print(int(x))  # konwersja do int
# print(long(x))
# print(float(x))
c = complex(x, y)
print(c.conjugate())  # sprzezona do danej zespolonej
print(divmod(x, y))  # para (x // y, x % y)
print(pow(x, y))  # x do potegi y
print(x ** y)  # x do potegi y
