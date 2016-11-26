import random
from datetime import datetime

a = range(0, 100000)
# print len(a), a[:100]
b = random.sample(a, 50000)
# print b

t1 = datetime.now()
najmn = 0
najwi = 0
# i = 0
# while i < len(b):
#     if b[najmn] > b[i]:
#         najmn = i
#     if b[najwi] < b[i]:
#         najwi = i
#     i += 1
najmn = 0
najwi = 0
for i in range(0, len(b)):
    if b[najmn] > b[i]:
        najmn = i
    if b[najwi] < b[i]:
        najwi = i

t2 = datetime.now()

print "minimum:", b[najmn]
print "maximum:", b[najwi]
print "time:   ", (t2 - t1).total_seconds() * 1000
