# Program do symulacji "Problemu Wolow Newtona" - w parametrach startowych programu nalezy podac
# liczbe morgow pola dostepnego do wypasu oraz liczbe tygodni przez jaki odbywa sie wypas.

import sys
import math

def input_get():
    print 'Program symulujacy problem \"Wolow Newtona\"\n'
    try:
        if sys.argv[1].isdigit() == False or sys.argv[2].isdigit() == False:
            print '\033[91mPodana wartosc nie jest liczba !!!\033[00m'
            exit(2)
    except Exception as exc:
        print exc
        print '\033[91mPodaj liczbe morgow oraz liczbe tygodni w parametrach startowych programu !!!\033[92m'
        exit(1)
    print "Liczba morgow do wypasu: %s\nLiczba tygodni: %s\n" % (sys.argv[1], sys.argv[2])
    return int(sys.argv[1]), int(sys.argv[2])

def print_grass(grass_amount):
    string_to_print = ''
    for i in range(0, grass_amount):
        string_to_print += ' \033[92m\\|/\033[00m '
    print string_to_print

def print_cow(cow_ammount):
    cow_layers = [' \033[95m((...))\033[00m ', ' \033[95m( O O )\033[00m ', '  \033[95m\   /\033[00m  ', '  \033[95m(`_`)\033[00m  ']
    for layer in cow_layers:
        string_to_print = ''
        for i in range(0, cow_ammount):
            string_to_print += layer
        print string_to_print

def main():
    field, grow_time = input_get()
    print "Poczatkowa ilosc jednostek trawy to 4 * ilosc morgow, w naszym przypadku to %d" % (field * 4)
    print_grass(field * 4)
    print "W ciagu %s tygodni urosna dodatkowe jednostki trawy w ilosci: %d" % (grow_time, field * grow_time)
    print_grass(field * grow_time)
    print "\nLaczna ilosc trawy do wypasu to : \033[92m%d\033[00m\n" % (field * 4 + field * grow_time)
    print 'Jeden wol zjada 2 jednostki trawy tygodniowo\n'
    calc =int(math.ceil(((field * 4.0) + (field * grow_time)) / (grow_time * 2.0)))
    print "Do pelnego wypasu potrzeba wolow w ilosci: \033[95m%d\033[00m" % calc
    print_cow(calc)

if __name__ == "__main__":
    main()