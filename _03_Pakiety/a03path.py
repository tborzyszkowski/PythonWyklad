import sys

print sys.path

# import pierwszy
# import drugi

sys.path.append('C:\home\gitHub\PythonWyklad\_03_Pakiety\moduly')

print sys.path

import pierwszy
import drugi

dir(pierwszy)
dir(drugi)


# Zadanie:
#  Zbuduj program skladajacy sie z dwoch katalogow,
#  po dwa moduly w kazdym katalogu.
#  Umozliwic ladowanie wszystkich modulow
#  do modulu glownego poslugujac sie zmienna PYTHONPATH
