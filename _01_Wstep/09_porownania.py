# porownania

print '----------'
print (1, 2, 3)	< (1, 2, 4)
print [1, 2, 3] <	[1, 2, 4]
print 'ABC' < 'C' < 'Pascal' < 'Python'
print (1, 2, 3, 4) < (1, 2, 4)
print (1, 2) < (1, 2, -1)
print (1, 2, 3) == (1.0, 2.0, 3.0)
print (1, 2, ('aa', 'ab')) < (1, 2, ('abc', 'a'), 4)

print '--- inne ---'
print (1, 2, 3)	< [1, 2, 3]
print (1, 2, 3)	> [1, 2, 3]
print 0 == 0L == 0.0 == 0j
print 'Ala' > ['A', 'l', 'a']
print 0 > [0]  # wynik tego typu porownan moze sie zmieniac z wersji na wersje
#               parz Reference manual
