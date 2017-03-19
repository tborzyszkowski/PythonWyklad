def mult(m1, m2):
    result = [[0, 0], [0, 0]]
    result[0][0] = m1[0][0]*m2[0][0] + m1[0][1]*m2[1][0]
    result[0][1] = m1[0][0]*m2[0][1] + m1[0][1]*m2[1][1]
    result[1][0] = m1[1][0]*m2[0][0] + m1[1][1]*m2[1][0]
    result[1][1] = m1[1][0]*m2[0][1] + m1[1][1]*m2[1][1]
    return result


def fibMatrixPower(m, n):
    if n == 1:
        return m
    elif n % 2 == 0:
        return fibMatrixPower(mult(m, m), n / 2)
    else:
        return mult(m, fibMatrixPower(mult(m, m), (n-1) / 2))


def fibonacciFast(n):
    result = [[1, 1], [1, 0]]
    return fibMatrixPower(result, n)[0][1]
