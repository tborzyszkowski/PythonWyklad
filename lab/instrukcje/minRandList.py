import random

a = range(0, 100)
print len(a), a[:10]
b = random.sample(a, 10)
print b

najmn = b[0]
i = 0
while i < len(b):
    if najmn > b[i]:
        najmn = b[i]
    i += 1

print "minimum:", najmn
