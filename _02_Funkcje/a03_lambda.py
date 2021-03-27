# a03_lambda
#
# przyklady lambda wyrazen

############################
# proste przyklady
from functools import reduce

f = (lambda x: x + 1)
print(f(1), (lambda x: x + 1)(3))


# dziala jak


def f(x):
    return x + 1

# Jakie sa roznice pomiedzy powyzszymi funkcjami?

############################
# niestety lambda wyrazenia w Pythonie nie sa w palni zgodne z
# teoria lambda-rachunku
# Sprobuj
# (lambda x, y: y)(lambda y: y)
# oraz
# print ((lambda x, y: y)((lambda y: y), 1))
print ((lambda x, y: x)((lambda y: y), 1)(5))


# Jak widac lista parametrow odpowiada raczej krotce parametrow,
# niz wielokrotnemu zastosowaniu
# ale mozna pierwsza linie zapisac tak
print(((lambda x: (lambda y: y))(lambda y: y))("Ala"))

############################
# W lambda-rzchunku  mozemy wyrazic wiekszosc dobrze znanych bytow

tt = (lambda x: (lambda y: x))
ff = (lambda x: (lambda y: y))
jesli = (lambda b: (lambda x: (lambda y: (b(x))(y))))

# jaka jest wartosc wyrazen
print(((jesli(tt))(1))(2))
print(((jesli(ff))(1))(2))

# Zadanie z wykladu
#   Sprobowac wyrazic w Pythonowym lambda-rachunku:
#   a) pary i rzutowania
#   b) liczby naturalne

############################
# narzedzia programowania funkcyjnego
#
# filter(f, lista) = lista elementow e takich, ze f(e)=true


def fff(x):
    return x % 2 != 0 and x % 3 != 0


print(filter(fff, range(2, 25)))
print(filter((lambda x: x % 2 != 0 and x % 3 != 0), range(2, 25)))
print ([el for el in filter((lambda x: x % 2 == 0 and x % 3 != 0), range(2, 25))])

# map(f, lista) = "f(lista)" = [f(e) for e in lista]


def cube(x):
    return x*x*x


print([el for el in map(cube, range(1, 11))])

# funkcja moze miec wiecej niz jeden argument
seq = range(8)


def add(x, y):
    return x+y


print([el for el in map(add, seq, seq)])
print([el for el in map((lambda x, y: x + y), seq, seq)])


# reduce(f, lista) = wylicza f(x,y) na kolejnych elementach listy 'sumujac ja'


def add(x, y):
    return x+y


print([el for el in reduce(add, range(1, 11))])


# przyklad sumowania list


def sum(seq):
    def add(x, y):
        return x+y
    return reduce(add, seq, 0)


print(sum(range(1, 11)))

print(sum([]))
