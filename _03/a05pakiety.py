import sys
sys.path.append('D:\users\Tomek\UG\Zajecia\Python\Wyklad\src\_03')

import pakiet
dir(pakiet)
from pakiet import *
dir(pakiet)
dir(pierwszy)

import pakiet.pierwszy
dir(pakiet)
dir(pakiet.pierwszy)
from pakiet.pierwszy import *
dir(pakiet)
dir(pakiet.pierwszy)
dir(pakiet.pierwszy.jeden_1)

import pakiet.trzeci
dir(pakiet)
dir(pakiet.trzeci)
from pakiet.trzeci import *
dir(pakiet)
dir(pakiet.trzeci)
from pakiet.trzeci import trzy_2, trzy_3
dir(pakiet.trzeci)


# Jakie sa roznice w uzyciu komend:
# import oraz from ... import do pakietow
# na ich poszczegolych poziomach?
