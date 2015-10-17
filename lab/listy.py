# a = []
# b = [1, a]
# print b
# b[1].append(1)
# print b, a
# a[0] = 5
# print b, a
# a.append(9)
# print b, a

w1 = [1,2,3,5,'Ala']
w2 = [3,4,5,8,'As']

print [w1[i]+w2[i] for i in range(len(w1))]

print range.__doc__
print range(1,10,5)