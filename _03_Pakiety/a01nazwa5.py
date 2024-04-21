from a01nazwa import nazwa
import a01nazwa

print(__name__)
a = 15


def nazwa():
    print(__name__)
    print("aqq = ", a)


def nazwa():
    print(__name__)
    print("aqqqq = ", a)
    print(a01nazwa.nazwa())


if __name__ == '__main__':
    a01nazwa.nazwa()
    nazwa()

