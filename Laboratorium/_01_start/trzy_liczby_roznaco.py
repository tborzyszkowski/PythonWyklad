counter = 0
for a in range(1, 8):
    for b in range(a+1, 9):
        for c in range(b+1, 10):
            counter += 1
            if a < b < c:
                pass
                # print(str(a)+str(b)+str(c))

print(counter)

counter = 0
for a in range(1, 9, 1):
    for b in range(2, 9, 1):
        for c in range(3, 10, 1):
            counter += 1
            if a < b < c:
                pass
                # print(str(a)+str(b)+str(c))

print(counter)
