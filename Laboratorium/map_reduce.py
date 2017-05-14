lista = [1.01, 2, 3, 4, 5]

print map((lambda x: x*x), lista)

print reduce((lambda x, y: x ** y), lista)
