# -*- coding: utf-8 -*-

import xlrd
from scipy import stats
import numpy as np


def parse_file(datafile):
    book = xlrd.open_workbook(datafile)
    sheet = book.sheet_by_index(0)

    data = [[sheet.cell_value(r, col)
                for col in range(sheet.ncols)]
                    for r in range(sheet.nrows)]

    print "\nList Comprehension"
    print "data[3][2]:",
    print data[3][2]

    print "\nCells in a nested loop:"
    for row in range(sheet.nrows):
        for col in range(sheet.ncols):
            if row == 50:
                print sheet.cell_value(row, col),


    print "\nROWS, COLUMNS, and CELLS:"
    print "Number of rows in the sheet:",
    print sheet.nrows
    print "Type of data in cell (row 3, col 6):",
    print sheet.cell_type(3, 6)
    print "Value in cell (row 3, col 6):",
    print sheet.cell_value(3, 6)
    print "Get a slice of values in column 6, from rows 1-3:"
    print sheet.col_values(6, start_rowx=1, end_rowx=4)

    return data

def xls_to_list(path,col_list):
    book = xlrd.open_workbook(path)
    sheet = book.sheet_by_index(0)

    data = [[sheet.cell_value(r, col)
                for col in range(sheet.ncols) if col in col_list]
                    for r in range(sheet.nrows)]
    return data



if __name__ == "__main__":
    path = '_0Stat_distr\PLLOTOS00025.xls'
    parse_file(path)
    print "#"*20
    dane = xls_to_list(path, [1]+range(5,13))
    print "Kursy otwarcia:"
    kurs_otwarcia_lst =[]
    for row in dane[1:]:
        #print row[0], row[1]
        kurs_otwarcia_lst.append(row[1])

    kurs_otwarcia_arr = np.array(kurs_otwarcia_lst).astype(np.float)
    n, (smin, smax), sm, sv, ss, sk = stats.describe(kurs_otwarcia_arr)
    sstr = 'mean = %6.4f, variance = %6.4f, skew = %6.4f, kurtosis = %6.4f'
    print 'LOTOS params:'
    print sstr %(sm, sv, ss, sk)

######################################
# Zadania
# 1. Ze strony
#    http://gpwinfostrefa.pl/GPWIS2/pl/quotes/archive/1
#    pobierz dane kilu innych instrumentow w zadanym przedziale czasowym,
#    a) oczytaj dane z interesujących Cię kolumn
#    b) wykonaj obliczenia statystyczne
