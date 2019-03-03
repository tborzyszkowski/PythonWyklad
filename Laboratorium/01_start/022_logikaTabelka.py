fst = [True, False]
snd = [True, False]
thd = [True, False]
fou = [True, False]

for p in fst:
    for d in snd:
        for t in thd:
            for c in fou:
                w1 = p or d and t and not c
                w2 = p or  (( d and t ) and ( not c ) )
                # w2 = ((p or d) and t) and (not c)
                if not w1 == w2:
                    print p, d, t, c

# print 0 or 'a' and 1 and not 0.0