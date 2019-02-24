fst = [True, False]
snd = [True, False]
thd = [True, False]

for p in fst:
    for d in snd:
        for t in thd:
            print p, d, t, p or d and t, p or (d and t)

# print 0 or 'a' and 1 and not 0.0