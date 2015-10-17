
def mult(m1, m2):
    n = len(m1)
    tmp = [[0 for i in range(n)] for j in range(n)]
    val = 0
    for i in range(n):
        for j in range(n):
            for c in range(n):
                val += m1[i][c] * m2[c][j]
            tmp[i][j]=val
            val = 0
    return tmp

a = [[1,1],[1,0]]

b = a

n = 6
while n-1:
    print b
    b = mult(b,a)
    n -=1
print b