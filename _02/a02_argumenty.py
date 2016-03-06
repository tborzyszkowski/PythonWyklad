# 02_argumenty
#
##########################################


def test1(a, b=1, c=2):
    print 'a : ', a, ' b : ', b, ' c : ', c

# Wykonaj
# test1(0)
# test1(5, 6)
# test1(6, c=7)
# test1(c=0, b=-1, a=-2)
# test1(b=3, c=4)

##########################################
# Argumenty domyslne sa wyliczane/inicjalizowane tylko raz

i = 1


def f(a=i):
    print 'a = ', a

i = 2
# print "f():", f()
# Jaki bedzie wynik powyzszego wywolania

##########################################
# Argumenty (takze domyslne) sa referencjami do obiektow (czasem zmiennych)


def g(a, L=[]):
    L.append(a)
    return L

print g(1)
print g(2)
print g(3)

# jaki tu otrzymamy rezultat - wyjasnij


def h(a, L=None):
    if L is None:
        L = []
    L.append(a)
    return L

print h(1)
print h(2)
print h(3)

##########################################
# Jako parametrow funkcji moza uzywac rowniez:
# - *nazwa - oznacza krotke argumentow przekazanych do funkcji
# - **nazwa - oznacza slownik o kluczach bedacych parametrami funkcji
# a wartosciach bedacych wartosciami przyporzadkowanymi tym parametrom


def pp(x, *arguments, **keywords):
    print 'x = ', x
    print '-' * 10
    print keywords
    print arguments
    keys = keywords.keys()
    keys.sort()
    for k in keys:
        print k, ' : ', keywords[k]

# Sprobuj
pp(1)
pp('aaa', b='bbb', c='ccc')
# pp(a='xxx', y='yyy', z='zzz', v='vvv')
pp('xxx', 'yyy', z='zzz', v='vvv')


def printf(format, *args):
    print format % args

# Sprobuj
printf('%s - %.3f', 'As', 123.45)

# operator * moze byc takze uzywany do rozpakowywania argumentow
# zgromadzinych w strukturach takich jak lista w celu uzycia ich komponentow
# jako argumentow funkcji
# Sprobuj
print range(3, 10, 2)
# oraz
lista = [3, 6]
range(*lista)
