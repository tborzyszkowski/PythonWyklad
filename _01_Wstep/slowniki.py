# slowniki

print '----------'
d = {'ab': 12, 33:{1:'q', 2:'w'}, 'bb':'cc'}

# typ slownika
print type(d)

# operacje
print d
d['z'] = 'zzz'
print d
d['z'] = 'qqq'
print d
# kasowanie
del d['z']
print d
d.clear()

# metody dostepne dla typu dict
print dir(dict)
