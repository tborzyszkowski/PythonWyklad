
cases = ((1, True), (2, False), (13, False), (64, True), (997, False), (1001*1001, True))

# ================
for case in cases:
    N = case[0]
    result = False
    i = 0

    while i <= N and not result:
        if i*i == N:
            result = True
        i += 1

    print(case, ": ", result == case[1])
#================

