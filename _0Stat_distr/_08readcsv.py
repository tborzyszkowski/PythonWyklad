# -*- coding: utf-8 -*-

import csv
from scipy import stats
import numpy as np

def csv_to_list(path, col_list):
    with open(path) as csvfile:
        csv_rows = csv.reader(csvfile, delimiter=';', quotechar='|')
        data = [[col
                    for col in row if row.index(col) in col_list]
                        for row in csv_rows]
    return data


if __name__ == "__main__":
    path = '_0Stat_distr\PLLOTOS00025.csv'
    dane = csv_to_list(path, [1]+range(5,13))

    print "##########################"
    for row in dane:
        print row

    kurs_otwarcia_lst =[]
    for row in dane[1:]:
        kurs_otwarcia_lst.append( float(row[1].replace(',','.')) )

    kurs_otwarcia_arr = np.array(kurs_otwarcia_lst).astype(np.float)
    n, (smin, smax), sm, sv, ss, sk = stats.describe(kurs_otwarcia_arr)
    sstr = 'mean = %6.4f, variance = %6.4f, skew = %6.4f, kurtosis = %6.4f'
    print 'LOTOS params:'
    print sstr %(sm, sv, ss, sk)

######################################
# Zadania
# 1. Ze strony
#    http://gpwinfostrefa.pl/GPWIS2/pl/quotes/archive/1
#    pobierz dane kilu innych instrumentow w zadanym przedziale czasowym.
#    a) zapisz dane w formacie csv (separator ";")
#    b) oczytaj dane z interesujących Cię kolumn
#    c) wykonaj obliczenia statystyczne na danych
#    UWAGA: sprawdź jakiego typu są odczytane wartości
