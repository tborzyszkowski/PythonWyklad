import sys

print(sys.path)

# import pierwszy
# import drugi

sys.path.append(r'C:\home\gitHub\PythonWyklad\_03_Pakiety\moduly')

print(sys.path)

import moduly.pierwszy
import moduly.drugi

dir(moduly.pierwszy)
dir(moduly.drugi)


# Zadanie:
#  Zbuduj program skladajacy sie z dwoch katalogow,
#  po dwa moduly w kazdym katalogu.
#  Umozliwic ladowanie wszystkich modulow
#  do modulu glownego poslugujac sie zmienna PYTHONPATH
