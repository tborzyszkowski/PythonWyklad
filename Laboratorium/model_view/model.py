N = 3
data = [[0 for _ in range(N)] for _ in range(N)]


def init():
    global data
    for j in range(N):
        for i in range(N):
            data[j][i] = 0


def setX(i, j):
    global data
    data[i][j] = 1


def setO(i, j):
    global data
    data[i][j] = 2

def the_same_in_some_row(who):
    the_same = True
    for row in data:
        for i in range(len(row)):
            if row[i] != who:
                the_same = False
                break
    return the_same

def who_win():
    global data
    return 1 if the_same_in_some_row(1) else 2
