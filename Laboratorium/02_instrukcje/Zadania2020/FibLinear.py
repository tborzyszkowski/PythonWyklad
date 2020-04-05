import time
import matplotlib.pylab as plt


def fibonacci_rek(n):
    if n < 2:
        return n
    else:
        return fibonacci_rek(n-2) + fibonacci_rek(n-1)


def fibonacci_linear(n):
    f1 = 0
    f2 = 1
    k = n - 2
    if n < 2:
        f2 = n
    else:
        while k >= 0:
            f2, f1, k = f1 + f2, f2, k-1
    return f2

#
# fast matrix multiplication
#

def mult(m1, m2):
    result = [[0, 0], [0, 0]]
    result[0][0] = m1[0][0]*m2[0][0] + m1[0][1]*m2[1][0]
    result[0][1] = m1[0][0]*m2[0][1] + m1[0][1]*m2[1][1]
    result[1][0] = m1[1][0]*m2[0][0] + m1[1][1]*m2[1][0]
    result[1][1] = m1[1][0]*m2[0][1] + m1[1][1]*m2[1][1]
    return result


def fibonacci_matrix_power(m, n):
    if n == 1:
        return m
    elif n % 2 == 0:
        return fibonacci_matrix_power(mult(m, m), n / 2)
    else:
        return mult(m, fibonacci_matrix_power(mult(m, m), (n-1) / 2))


def fibonacci_fast(n):
    result = [[1, 1], [1, 0]]
    return fibonacci_matrix_power(result, n)[0][1]


fibs = [fibonacci_fast]

results = {f.__name__: [] for f in fibs}
print results

step = 5000
r_begin = 2000*1000
r_end = r_begin + 100 * step
r_range = range(r_begin, r_end, step)

for idx in r_range:
    print "idx =", idx,
    for f in fibs:
        start_time = time.clock()
        f(idx)
        czas = time.clock() - start_time
        results[f.__name__].append(czas)
        print czas, "\t",
    print "\n"
print results


# plt.plot(r_range, results["fibonacci_linear"], linestyle='-', color='b')
plt.plot(r_range, results["fibonacci_fast"], linestyle='-', color='r')
plt.show()
