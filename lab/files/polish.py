# -*- coding: utf-8 -*-

polish_list = [u'ą', u'ć', u'ę', u'ł', u'ń', u'ó', u'ś', u'ź', u'ż'] + \
    [chr(a) for a in range(ord('a'), ord('z')+1)] + \
    [u' ']

# u = u'idzie wąż wąską dróżką'
# uu = u #.decode('utf8')
# print uu.encode('utf8')

tekst = u'idzie wąż wąską dróżką'

wynik = ''.join(i for i in tekst if i in polish_list)
# for i in tekst:
#      print i.encode('utf8')

# print unicode('ą').encode('utf8')
print wynik.encode('utf8')
