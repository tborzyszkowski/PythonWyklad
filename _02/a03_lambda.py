# a03_lambda
#
# przyklady lambda wyrazen

############################
# proste przyklady
f = (lambda x: x + 1)
print f(1)
# dziala jak

def f(x):
    return x + 1

# Jakie sa roznice pomiedzy powyzszymi funkcjami?

############################
# niestety lambda wyrazenia w Pythonie nie sa w palni zgodne z
# teoria lambda-rachunku
# Sprobuj
#(lambda x, y: y)(lambda y: y)
# oraz
(lambda x, y: y)((lambda y: y), 1)

# Jak widac lista parametrow odpowiada raczej krotce parametrow,
# niz wielokrotnemu zastosowaniu
# ale mozna pierwsza linie zapisac tak
(lambda x: (lambda y: y))(lambda y: y)

############################
# W lambda-rzchunku  mozemy wyrazic wiekszosc dobrze znanych bytow

tt = (lambda x: (lambda y: x))
ff = (lambda x: (lambda y: y))
jesli = (lambda b: (lambda x: (lambda y: (b (x) )(y))))

# jaka jest wartosc wyrazen
((jesli (tt))(1))(2)
((jesli (ff))(1))(2)

# Zadanie z wykladu
#   Sprobowac wyrazic w Pythonowym lambda-rachunku:
#   a) pary i rzutowania
#   b) liczby naturalne

############################
# narzedzia programowania funkcyjnego
#
# filter(f, lita) = lista elementow e takich, ze f(e)=true
def fff(x):
    return x % 2 != 0 and x % 3 != 0

filter(fff, range(2, 25))

# map(f, lista) = f(lista)
def cube(x):
    return x*x*x

map(cube, range(1, 11))

# funkcja moze miec wiecej niz jeden argument
seq = range(8)
def add(x, y):
    return x+y

map(add, seq, seq)

# reduce(f, lista) = wylicza f(x,y) na kolejnych elementach listy 'sumujac ja'
def add(x,y):
    return x+y

reduce(add, range(1, 11))

# przyklad sumowania list
def sum(seq):
    def add(x,y):
        return x+y
    return reduce(add, seq, 0)
 
sum(range(1, 11))

sum([])

