
w1 = [1, 1, 1]
w2 = [2, 2, 2]

print reduce(lambda x, y: x+y,
             [w1[i]*w2[i] for i in range(0, len(w1))]
             )
