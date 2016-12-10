import math

a = 1


def test1(arg1):
    """To jest pierwsza linia opisu

    A to sa kolejne
    I jeszcze
    I jeszcze.
    """
    global a
    a = arg1
    print 'test1: LOCALS  :', locals()
    print 'test1: GLOBALS :', globals()


#####################################################
# print 'test1: GLOBALS :', globals()
# test1(3)
# print 'test1: GLOBALS :', globals()

# print test1.__doc__
#
# print math.sin.__doc__
# print locals.__doc__
# print globals.__doc__

print a
globals()['a'] = 5
print a
