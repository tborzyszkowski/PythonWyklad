# Czy podana liczba N jest kwadratem innej liczby naturalnej

N = 1000000
isSquare = False

squareCandidate = 1
counter = 0
while (squareCandidate * squareCandidate <= N) and not isSquare:
    if squareCandidate * squareCandidate == N:
        isSquare = True
    else:
        squareCandidate += 1
    counter += 1

if isSquare:
    print "TAK"
else:
    print "NIE"
print "Counter:", counter
