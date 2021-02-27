# slowniki

d = {'ab': 12, 33: {1: 'q', 2: 'w'}, 'bb': 'cc'}

print(list(d.values()))
print(list(d.keys()))

# typ slownika
print(type(d))
print(len(d[33]))

# operacje
print(d)
d['z'] = 'zzz'
print(d)
d['z'] = 'qqq'
print(d)

# kasowanie
del d['z']
print(d)
d.clear()
print(d)

# metody dostepne dla typu dict
print(dir(dict))
