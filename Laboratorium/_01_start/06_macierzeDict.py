from random import randint

n = 2
m1 = {w: {k: randint(0, 5) for k in range(n)} for w in range(n)}
# m2 = {w: {k: (1 if w == k else 0) for k in range(n)} for w in range(n)}
m2 = {w: {k: randint(0, 5) for k in range(n)} for w in range(n)}
wyn = {w: {k: 0 for k in range(n)} for w in range(n)}

for w in range(n):
    for k in range(n):
        for c in range(n):
            wyn[w][k] += m1[w][c]*m2[c][k]

for w in range(n):
    print(m1[w].values())
print

for w in range(n):
    print(m2[w].values())
print

for w in range(n):
    print(wyn[w].values())

######
# List version

print("-- List version --")

n = 2
m1 = [ [randint(0, 5) for k in range(n)]  for w in range(n) ]
m2 = [ [randint(0, 5) for k in range(n)]  for w in range(n) ]
wyn = [ [0 for k in range(n)] for w in range(n)]

for w in range(n):
    for k in range(n):
        for c in range(n):
            wyn[w][k] += m1[w][c]*m2[c][k]

for w in range(n):
    print(m1[w])
print

for w in range(n):
    print(m2[w])
print

for w in range(n):
    print(wyn[w])
