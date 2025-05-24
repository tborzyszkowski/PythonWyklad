import csv
# import statistics
from matplotlib import pyplot as plt
from scipy.interpolate import interp1d
import numpy as np

# print(float("3.14"))

with open('pknorlen_akcje.csv') as csvfile:
    readCSV = csv.reader(csvfile, delimiter=',')
    next(readCSV)
    counter = 0
    kursy_lista = []
    for row in readCSV:
        kursy_lista.append({"data": row[0], "kurs_max": float(row[5]), "kurs_min": float(row[6])})
        counter += 1
        # if counter > 10:
        #     break

print(counter)
# print("Srednia: ", statistics.mean([k["kurs_max"] for k in kursy_lista]))
# print("Odch.Std:", statistics.stdev([k["kurs_max"] for k in kursy_lista]))
# print([k["kurs_max"] for k in kursy_lista])
print("Max1: ", max([k["kurs_max"] for k in kursy_lista]))
print("Max2: ", max(kursy_lista, key=lambda x: x["kurs_max"]))
print("Min:", min([k["kurs_max"] for k in kursy_lista]))

# y_es = [k["kurs_max"] for k in kursy_lista]
# x_es = range(0,len(y_es))
#
# f_linear = interp1d(x_es, y_es, kind='quadratic')
# xnew = np.linspace(0, len(y_es), 100)
#
# plt.plot(x_es, y_es, 'o',
#     xnew, f_linear(xnew), '-')
# plt.show()