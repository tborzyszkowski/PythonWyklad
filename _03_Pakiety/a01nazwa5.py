print __name__
a = 15


def nazwa():
    print __name__
    print "aqq = ", a


def nazwa():
    print __name__
    print "aqqqq = ", a

# wyprobuj:
import a01nazwa
a01nazwa.nazwa
a01nazwa.nazwa()
nazwa()

from a01nazwa import nazwa
nazwa()
