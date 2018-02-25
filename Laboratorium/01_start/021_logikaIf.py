
valLog = [None, True, False]
valA = [None, 1]
valB = [None, 2]

for v in valLog:
    for a in valA:
        for b in valB:
            print "v:", v, "a:", a, "b:", b, (v and [a] or [b])[0], v and a or b, a if v else b