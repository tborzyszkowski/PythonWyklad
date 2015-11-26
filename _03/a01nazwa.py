print __name__
# print type(__name__)

a = 13


def nazwa():
    print __name__
    a = 1
    print "a = ", a


# wyprobuj:
#  import a01nazwa
#  a01nazwa.nazwa
if __name__ == "__main__":
    print 'aqq'
    nazwa()
    print 'a = ', a
