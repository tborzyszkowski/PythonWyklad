def in_carpet(x, y):
    while True:
        if x == 0 or y == 0:
            return True
        elif x % 3 == 1 and y % 3 == 1:
            return False
 
        x /= 3
        y /= 3
 
def carpet(n):
    for i in range(3 ** n):
        for j in range(3 ** n):
            if in_carpet(i, j):
                print('*')
            else:
                print(' '),
        print("\n")

carpet(3)