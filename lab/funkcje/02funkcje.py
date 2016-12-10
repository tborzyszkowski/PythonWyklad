# def test1(a, b=1, c=2):
#     print 'a : ', a, ' b : ', b, ' c : ', c
#
# # Wykonaj
# test1(0)
# test1(5, 6)
# test1(6, c=7)
# test1(c=0, b=-1, a=-2)
# test1(b=3, c=4)

# i = 1
#
# def f(a = i):
#     print 'a = ', a
#
# f()
# i = 2
# f()


#
# def g(a, L=[]):
#     # L=[]
#     L.append(a)
#     return L
#
# QQ = [11, 22, 33]
# print g(1, QQ)
# print g(2, QQ)
# print g(3, QQ)
#
#
# def h(a, L=None):
#     if L is None:
#         L = []
#     L.append(a)
#     return L
#
# QQ = None
# print h(1, QQ)
# print h(2, QQ)
# print h(3, QQ)


def pp(x, *arguments, **keywords):
    print arguments, keywords
    for k in keywords:
        print k, keywords[k]
    for a in arguments:
        print a


# Sprobuj
pp(1)
pp('aaa', 'bbb', c = 'ccc')
# pp('qqq', a='xxx', y='yyy', z='zzz', v='vvv')
# pp('xxx', 'yyy', z='zzz', v='vvv')
