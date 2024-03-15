from decimal import *

epsilon = Decimal(1.0)
n = 0
eps = Decimal(epsilon)
limit = 1000 * 1000 * 10

while epsilon > 0.0 and n < limit:
    eps = epsilon
    epsilon /= Decimal(2)
    n += 1

print("Epsilon 0:", eps)
print("N:", n)
