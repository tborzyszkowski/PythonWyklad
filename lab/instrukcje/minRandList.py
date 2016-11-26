import random

a = range(0, 100)
print len(a), a[:10]
b = random.sample(a, 10)
print b

najmn = 0
najwi = 0
i = 0
while i < len(b):
    if b[najmn] > b[i]:
        najmn = i
    if b[najwi] < b[i]:
        najwi = i
    i += 1

print "minimum:", b[najmn]
print "maximum:", b[najwi]
