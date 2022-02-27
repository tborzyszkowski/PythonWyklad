epsilon = 1.0
n = 0
eps = epsilon
limit = 10 * 1000

while epsilon > 0.0 and n < limit:
    eps = epsilon
    epsilon /= 2
    n += 1

print("Epsilon 0:", eps)
print("N:", n)


number = 10**100 * 1.0
epsilon = number
n = 0
eps = epsilon
limit = 10 ** 6

while epsilon + number > number and n < limit:
    eps = epsilon
    epsilon /= 2
    n += 1

print("Epsilon ", number, ":", eps)
print("N:", n)