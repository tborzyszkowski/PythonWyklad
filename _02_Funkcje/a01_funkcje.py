# 01_funkcje
#
# Sprobuj wykonac w shellu:
# locals()
# globals()
# import a01_funkcje
# locals()
# globals()
"""
Opis modulu
"""

a = 1
b = 2


def test1(arg1):
    """To jest pierwsza linia opisu

    A to sa kolejne
    I jeszcze
    I jeszcze.
    """
    a = arg1
    print 'test1: LOCALS  :', locals()
    print 'test1: GLOBALS :', globals()['a']


def test2(arg2):
    """Test2_doc
    """
    # global a
    a = arg2
    b = arg2 + 1
    test1(b)
    print 'test2:LOCALS  :', locals()
    print 'test2:GLOBALS :', globals()['a']

print a, b
# test1(3)
# print '--------------'
# test2(3)
# print a, b
#
# print test1.__doc__
# print test2.__doc__
#
# print locals.__doc__
# print globals.__doc__

# locals()['a'] = 5
# print locals()['a'], a

# print globals()['a']
# globals()['a'] = 6
# print globals()['a']

# print globals()['z']
# globals()['z'] = 6
# print globals()['z'], z

# nastepnie sprawdzmy wyniki
# import a01_funkcje
#
# a01_funkcje.a
# a01_funkcje.b
# a01_funkcje.test1(3)
# a01_funkcje.test2(3)

# jakie wyniki otrzymamy wywolujac
# 01_funkcje.test1.__doc__
# 01_funkcje.test2.__doc__
#
# Sprawdz
# locals.__doc__
# globals.__doc__
