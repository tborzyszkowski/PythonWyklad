# 01_funkcje
#
# Sprobuj wykonac w shellu:
# locals()
# globals()
# import a01_funkcje
# locals()
#
"""
Opis modulu
"""

a = 1
b = 2


def first_try(arg1):
    """
    Opis funcji

    :param arg1: pierwszy parametr funkcji
    :return: brak wartosci zwracanej
    """
    a = arg1
    global b
    b = arg1 + 1
    print('test1: LOCALS   :', locals())
    print('test1: GLOBALS a:', globals()['a'])
    print('test1: GLOBALS b:', globals()['b'])


def second_try(arg2):
    """Test2_doc
    """
    global a
    a = arg2
    b = arg2 + 1
    first_try(b)
    a += 1
    print('test2:LOCALS  :', locals())
    print('test2:GLOBALS :', globals()['a'])


if __name__ == "__main__":
    print(a, b)
    first_try(3)
    print('--------------')
    second_try(7)
    print(a, b)

    print(first_try.__doc__)
    print(second_try.__doc__)

    print(locals.__doc__)
    print(globals.__doc__)

    locals()['a'] = 5
    print(locals()['a'], a)

    print(globals()['a'])
    globals()['a'] = 6
    print(globals()['a'])

    # print(globals()['z'])
    # globals()['z'] = 6
    # print(globals()['z'], z)

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
