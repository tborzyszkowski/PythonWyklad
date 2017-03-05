d = {v: v**2 for v in range(1, 10, 2)}

print d
print d.iteritems()
print d.values()

for ind in d:
    print ind, d[ind]

for ind, val in d.iteritems():
    print ind, val

for val in d.values():
    print val

for ind in d.keys():
    print ind
