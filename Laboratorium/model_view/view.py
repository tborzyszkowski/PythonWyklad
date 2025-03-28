from model import *


def print_desk():
    global data
    for j in range(len(data)):
        for i in range(len(data[j])):
            print(data[j][i], end=" ")
        print()


def print_who_win():
    print(who_win())
