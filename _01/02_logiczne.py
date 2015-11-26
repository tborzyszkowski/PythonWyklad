# operacje logiczne

print '----------'
# wartosci uwazane za falsz
print None, False, 0, 0L, 0.0, 0j, '', (), [], {}

# wynikiem operacji logicznej jest wartosc odpowiedniego wyrazenia
print (None or 'napis')
print (None and 'napis')
print [1, 2, 3] or {1: 'aa', 4: 'qq'}
print [1, 2, 3] and {1: 'aa', 4: 'qq'}

# jaka bedzie wartosc wyrazenia ?
print 0 or 'a' and 1 and not 0.0

# leniwe wartosciowanie


def sidefx():
    print "in sidefx()"
    return 1


print 'a' or sidefx()
print 0 or sidefx()
