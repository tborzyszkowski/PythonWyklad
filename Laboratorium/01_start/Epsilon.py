epsilon = 1.0
n = 0
eps = epsilon
limit = 10 * 1000

while epsilon > 0.0 and n < limit:
    eps = epsilon
    epsilon /= 2
    n += 1

print "Epsilon:", eps
print "N:", n
