# from model import *
import model

def print_desk():
    #global model.data
    for j in range(len(model.data)):
        for i in range(len(model.data[j])):
            print(model.data[j][i], end=" ")
        print()


def print_who_win():
    print(model.who_win())
