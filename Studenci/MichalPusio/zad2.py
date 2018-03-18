def abc(x):
    x+2

def f1(a):
    while a < 100:
        a+1

def f2(b):
    while b < 100:
        b+1

print (1, 2, 3) < (1, 2, 4)
print [1, 2, 3] < [1, 2, 4]
print 'ABC' < 'C' < 'Pascal' < 'Python'
print (1, 2, 3, 4)<(1, 2, 4)
print (1, 2) < (1, 2, -1)
print (1, 2, 3) == (1.0, 2.0, 3.0)
print (1, 2, ('aa', 'ab')) < (1, 2, ('abc', 'a'), 4)

print (1, 2, 3) > sum((1, 2)) #funkcja zwraca wartosc 3, trzy nie jest wieksze od krotki
print (1, 2, 3) > "zzz" #pojedynczy string rowniez nie jest wiekszy od krotki
print 1 < "zzz" #ale sam string jest wiekszy od liczby
print abc(2) == None #funkcja bez return zwraca wartosc "None" jezeli ja porownac
print None < 0 #i None jest mniejsze od zera
print {} > 0 #pusty slownik jest wiekszy od zera

#wstepna chierarchia:
print None < 0 < 10000 < {} < {"a":3, "c": 12345} < [] < [1, 3, 4] < "a" < "z" < () < (3, 4, 1000)
#generalnie calosc od slownikow jest poukladana alfabetycznie
#dict<list<string<tuple
#jezeli typ nie rozstrzyga o wielkosci, (a raczej jego nazwa), to robia to jego wartosci