# Program do symulacji "Problemu Jozefa Flawiusza" - w parametrach startowych programu
# nalezy podac liczbe rycerzy bioracych udzial w symulacji.

import sys
print 'Program symulujacy problem Jozefa Flawiusza\n'
try:
    knights = sys.argv[1]
    if knights.isdigit() == False:
        print '\033[91mPodana wartosc nie jest liczba !!!\033[00m'
        exit(2)
except Exception as exc:
    print exc
    print '\033[91mPodaj liczbe rycerzy w parametrach startowych programu !!!\033[00m'
    exit(1)
print "Liczba rycerzy: %s" % knights

death_ring = []
for i in range(0, int(knights)):
    death_ring.append(i+1)

round_counter = 1

while len(death_ring) != 1:
    round_string = ""
    temporary_list = []
    print "\nRunda: %s\n" % round_counter
    for i in range(0, len(death_ring)):
        if i % 2 == 0:
            round_string += str(death_ring[i]) + " "
            temporary_list.append(death_ring[i])
        else:
            round_string += "\033[1;31;49m%s \033[00m" % str(death_ring[i])
    print round_string
    if len(death_ring) % 2 == 1:
        temporary_list.insert(0, temporary_list[-1])
        del temporary_list[-1]
    death_ring = temporary_list
    round_counter += 1

print "\nW kregu smierci zlozonym z %s rycerzy, lepiej zebys stal na \033[92m%d\033[00m miejscu !!!" % (knights, death_ring[0])