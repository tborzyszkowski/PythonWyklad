# a04_przyklad
#
##############################
# przyklad dzialania na liscie

from apihelper import info
li = []
info(li)

##############################
# przyklad dzialania na module

import math
info(math)
info(math, 30)
info(math, 20, 0)

##############################
# Funkcja: type
type(1)

li = []
type(li)

import apihelper
type(apihelper)

import types
type(apihelper) == types.ModuleType
type(types.ModuleType)

# type - funkcja bierze "cokolwiek" i oddaje tego typ "czegos"

##############################
# Funkcja: str

str(1)
str(apihelper)
str(None)

# str - daje reprezentacje napisowa dowolnego elementu

##############################
# Funkcja: dir

li=[]
dir(li)

d = {}
dir(d)

dir(apihelper)

# zawartosc obiektu

##############################
# Funkcja: callable

callable(apihelper)
callable(apihelper.info)

# oddaje True gdy obiekt mozna wywolac

##############################
# Funkcja: getattr

object = apihelper
method = "info"
getattr(object, method)
type(getattr(object, method))
type(getattr(object, method)) == types.FunctionType
callable(getattr(object, method))

# funkcja oddaje referencje do funkcji z obiektu, ktory jest pierwszym argumentem
# o nazwie, ktora jest drugim
# funkcje/metody w Pythonie sa obiektami (jak "prawie" wszystko)
# funkcja ta pozwala zbudowac referencje do funkcji, ktore powstana dopiero w czasie uruchomienia

##############################
# Funkcja: join, split

s = "Ala    ma\n kota\ti\tAsa."
print s
print s.split()
print " ".join(s.split())
print "\n".join(s.split())

##############################
# Powyzsze funkcje (i wiecej) pochodza z modulu __builtin__
# po uruchomieniu Pythona wszystkie funkcje tego modulu
# sa dostepne w biezacej przestrzeni nazw - tak jak by ktos wywolal niejawnie:
from __builtin__ import *

#info(__builtin__, 20)

