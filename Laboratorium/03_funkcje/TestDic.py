d = {"1": "a", "2": "b"}

l = d.keys()
l.append("x")

d2 = {}

for x in l:
    if x in d:
        d2[x] = d[x]

print d2