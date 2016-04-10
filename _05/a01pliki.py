# operacje na plikach

f = open('plik.txt', 'w')
print f

print '-'*20

f.write('1234567890abcdefghijk\n')
f.write('Ala ma kota\n')
t = ('a', 1, 3.14)
f.write(str(t))
f.write('\n')

f.close()

print f

print '-'*20

f = open('plik.txt', 'r')

print 'Pocz   : ', f.tell()
s = f.read(10)
print s
print 'Read 1 : ', f.tell()
print f.read()
print 'Read 2 : ', f.tell()
f.seek(-15, 2)
print f.read(3)
print 'Seek 2 : ', f.tell()
print f.read()

f.close()
