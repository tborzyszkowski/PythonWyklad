# a04_przyklad
#
##############################
# przyklad dzialania na liscie

from apihelper import info
# li = []
# print(info(li))

# ##############################
# # przyklad dzialania na module
#
import math
# print(info(math))
# print(info(math, 30))
# print(info(math, 20, 0))

# ##############################
# # Funkcja: type
# type(1)
#
# li = []
# print(type(li))
#
import apihelper
# print(type(apihelper))

import types
#
# print(type(apihelper) == types.ModuleType)
# print(isinstance(apihelper, types.ModuleType))
# print(type(types.ModuleType))
#
# # type - funkcja bierze "cokolwiek" i oddaje tego typ "czegos"
#
# ##############################
# # Funkcja: str
#
# print( str(1))
# print( str(apihelper) )
# print( str(None) )
#
# # str - daje reprezentacje napisowa dowolnego elementu
#
# ##############################
# # Funkcja: dir
#
# li = []
# print(dir(li))
#
# d = {}
# print(dir(d))
#
# print(dir(apihelper))
#
# # zawartosc obiektu
#
# ##############################
# # Funkcja: callable
#
# print(callable(apihelper))
# print(callable(apihelper.info))
#
# # oddaje True gdy obiekt mozna wywolac
#
# ##############################
# # Funkcja: getattr
#
# import types
# object = apihelper
# method = "info"
# print getattr(object, method)
# print type(getattr(object, method))
# print type(getattr(object, method)) == types.FunctionType
# print callable(getattr(object, method))
# print getattr(object, method)(1)
#
# # funkcja oddaje referencje do funkcji z obiektu, ktory jest pierwszym argumentem
# # o nazwie, ktora jest drugim
# # funkcje/metody w Pythonie sa obiektami (jak "prawie" wszystko)
# # funkcja ta pozwala zbudowac referencje do funkcji, ktore powstana dopiero w czasie uruchomienia
#
# ##############################
# # Funkcja: join, split
#
# s = "Ala    ma\n kota\ti\tAsa."
# print(s)
# print(s.split())
# print(" ".join(s.split()))
# print("\n".join(s.split()))
#
# ##############################
# # Powyzsze funkcje (i wiecej) pochodza z modulu __builtin__
# # po uruchomieniu Pythona wszystkie funkcje tego modulu
# # sa dostepne w biezacej przestrzeni nazw - tak jak by ktos wywolal niejawnie:
# from builtins import *
# import builtins
# print(dir(builtins))
#
# info(builtins, 20)
