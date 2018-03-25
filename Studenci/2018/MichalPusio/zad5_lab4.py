#zad 5
#Napisz funkcje o dowolnej liczbie argumentow, ktora oddaje najwiekszy z podanych argumentow.

def maks(*num):
    a = sorted(num)
    return a[-1]

def maks_reduce(*args):
    return reduce(maks, args)

#dziala dla liczb
a = maks(5, 4, 78, -256, 351)
print a

#dziala dla liczb i napisow
b = maks("siema", 4, 8, "witam")
print b

#hierarchia porownan
print None < 0 < 10000 < {} < {"a":3, "c": 12345} < [] < [1, 3, 4] < "a" < "z" < () < (3, 4, 1000)

c = maks(None, 4, 2000, (3, 5, 6), {}, [], {1:"a"}) #powinno zwrocic tuple, po porownaniu typu, bo typ "tuple" jest najwyzej alfabetycznie (patrz hierarchie)
print c

#sprawdzenie dla reduce
print maks_reduce(None, 4, 2000, (3, 5, 6), {}, [], {1:"a"})
