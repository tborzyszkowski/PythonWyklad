# krotki

k = ('a', 1, 'qqq', {1:'x', 2:'y'})
print k

print k[0]
print k[-1]
print k[1:-1]


print '------operacje ----------'
#k.append('www')
#k.remove('qq')
#k.index(1)
print 'a' in k, 'z' in k

# krotka jako lista
l = list(k)
print l
l[0] = 'x'
# i znow jako krotka
k = tuple(l)
print k

print dir(tuple)