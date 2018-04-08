import os

def cls():
    os.system('cls' if os.name=='nt' else 'clear')


products = {'dzem': {'cena': 2.5, 'ilosc': 12},
    'maslo': {'cena': 9, 'ilosc': 11},
    'mleko': {'cena': 2, 'ilosc': 122},
    'lambo': {'cena': 5856, 'ilosc': 2}}
basket = {}

def koszt():
    zakupy = 0
    for k in basket:
         zakupy += basket[k]['ilosc'] * basket[k]['cena']
    print 'Wartosc koszyka to: ', zakupy


def showbasket():
    print 'KOSZYK\n--------------\nnazwa\tcena\tilosc'
    for k in basket:
        print k, '\t', basket[k]['cena'],'\t', basket[k]['ilosc']
    koszt()

def whattodo():
    i = raw_input('Co chcesz zrobic? a - add b - basket, k - koniec: ')
    if i == 'b':
        cls()
        showbasket()
        whattodo()
    elif i == 'k':
        exit()
    elif i == 'a':
        cls()
        ask()

def showinventory():
    print '\nnazwa\tcena\tilosc'
    for k in products:
        print k, '\t', products[k]['cena'],'\t', products[k]['ilosc']


def ask():
    showinventory()
    item = raw_input('podaj nazwe: ')
    if item in products.keys():
        q = input('podaj ilosc: ')
        if q > 0 and q <= products[item]['ilosc']:
            print 'zamawiasz ', q, 'x ', item
            products[item]['ilosc'] -= q
            basket.update({item:{'cena' : products[item]['cena'], 'ilosc': q}})
        else:
            print 'nie ma tyle na stanie'
    else:
        print 'nie ma takiego produktu'
    whattodo()

whattodo()
