import sys

print sys.path

# import pierwszy
# import drugi

sys.path.append('D:\users\Tomek\UG\Zajecia\Python\Wyklad\PythonWyklad\_03\moduly')

print sys.path

import pierwszy
import drugi


# Zadanie:
#  Zbuduj program skladajacy sie z dwoch katalogow,
#  po dwa moduly w kazdym katalogu.
#  Umozliwic ladowanie wszystkich modulow
#  do modulu glownego poslugujac sie zmienna PYTHONPATH
