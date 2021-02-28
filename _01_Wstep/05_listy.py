# listy

print('----------')

l = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
print(l)
print(l[0])
print(l[-1])
print(l[1:6])
print(l[0:7])
print(l[0:8])
print(l[:5])
print(l[3:])
print(l[:])
print(l[7:2:-1])
print(l[7:2])
# print l[7]

print('------ wstawianie --------')
l.append('z')
print(l)

l.insert(2,'qq')
print(l)

l.extend(['x','y','z'])
print(l)

l.append(['x','y','z'])
print(l)

print(l[-1])

print(l.index('z'))

print(('z' in l), ('w' in l))

print('--------- usuwaie ---------')
print(l.pop())
print(l)
l.remove('qq')
print(l)

print('-------- operacje ----------')
l = l + ['Ala']
l += ['As']
print(l)

l = l * 2
print(l)

print(type(l))
print(dir(list))

# ----- jaki bedzie wynik ? -------
a = []
b = [1, a]
b[1].append(1)
print(a, b)

x = []
y = [1, x]
x.append(1)
print(x, y)


x = []
x.append(x)
print(x)
