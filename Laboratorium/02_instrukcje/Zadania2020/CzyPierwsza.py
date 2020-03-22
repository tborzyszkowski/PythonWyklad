# Czy podana liczba N jest liczba pierwsza

LIMIT = 1000
for N in range(2, LIMIT):
    isPrime = True
    potentialDivisor = 2
    counter = 0
    while (potentialDivisor < N / 2) and isPrime:
        if (N % potentialDivisor) == 0:
            isPrime = False
        else:
            potentialDivisor += 1
        counter += 1
    if isPrime:
        print "Prime number:", N, "Counter:", counter
