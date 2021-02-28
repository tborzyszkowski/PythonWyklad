# mapowanie list

print('----------')
# przyklad z wykladu
print([z ** 2 for z in range(10) if z % 2 == 0])

# prostszy przyklad
vec = [2, 4, 6]
print([3*x for x in vec])
print([3*x for x in vec if x > 3])
print([3*x for x in vec if x < 2])
print([[x, x**2] for x in vec])

# blad ale jaki ?
# print [x, x**2 for x in vec]
print([(x, x**2) for x in vec])

# bardziej zlozona skaldnia
vec1 = [2, 4, 6]
vec2 = [4, 3, -9]
print([x*y for x in vec1 for y in vec2])
print([x+y for x in vec1 for y in vec2])
print([vec1[i]*vec2[i] for i in range(len(vec1))])

print([str(round(355/113.0, i)) for i in range(1, 6)])
