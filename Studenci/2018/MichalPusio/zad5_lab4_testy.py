#--Ktora dziala najszybciej?
import time
def maks_pair(a, b):
    if a > b:
        return a
    else:
        return b

def maks(*num):
    a = sorted(num)
    return a[-1]

def maks_reduce(*args):
    return reduce(maks, args)

def maks_pair_reduce(*args):
    return reduce(maks_pair, args)

start = time.time()

print maks(None, 4, 2000, (3, 5, 6), {}, [], {1:"a"}) #powinno zwrocic tuple, po porownaniu typu, bo typ "tuple" jest najwyzej alfabetycznie (patrz hierarchie)
t1 = time.time() - start
print("--- %s seconds ---" % (t1))

#sprawdzenie dla reduce
print maks_reduce(None, 4, 2000, (3, 5, 6), {}, [], {1:"a"})
t2 = time.time() - t1
print("--- %s seconds ---" % (t2))

#calosc dziala rowniez dla porownania pary
print maks_pair_reduce(None, 4, 2000, (3, 5, 6), {}, [], {1:"a"})
print("--- %s seconds ---" % (time.time() - t2))

t2 = time.time()
lista_duza = range(0, 10000000)
print maks_pair_reduce(*lista_duza )
print("--- %s seconds ---" % (time.time() - t2))


t2 = time.time()
print maks_reduce(*lista_duza )
print("--- %s seconds ---" % (time.time() - t2))
