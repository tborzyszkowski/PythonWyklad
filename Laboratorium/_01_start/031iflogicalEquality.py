
przypadki = [(0, 0, 0),
             (0, 0, 1), (0, 1, 0), (1, 0, 0),
             (1, 1, 0), (1, 0, 1), (0, 1, 1),
             (1, 1, 1),]

for (a, b, c) in przypadki:
    if not (b and [a] or [c])[0] == (a if b else c):
        print (a, b, c)