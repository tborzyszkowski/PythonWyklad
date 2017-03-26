import random
from datetime import datetime

N = 10000
a = range(0, 100000)
b = random.sample(a, N)

t1 = datetime.now()
for i in range(0, N):
    for j in range(N-1, i, -1):
        if b[j-1] > b[j]:
            b[j-1], b[j] = b[j], b[j-1]
t2 = datetime.now()
# print b[:N / 10]
print "time:   ", (t2 - t1).total_seconds() * 1000

b = random.sample(a, N)
t1 = datetime.now()
sorted(b)
t2 = datetime.now()
# print b[:N / 10]
print "time:   ", (t2 - t1).total_seconds() * 1000
