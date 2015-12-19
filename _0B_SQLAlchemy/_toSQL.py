# -*- coding: utf-8 -*-

import sqlite3
import csv

def csv_to_list(path, col_list):
    with open(path) as csvfile:
        csv_rows = csv.reader(csvfile, delimiter=';', quotechar='|')
        data = [[col
                    for col in row if row.index(col) in col_list]
                        for row in csv_rows]
    return data

if __name__ == "__main__":
    path = '_0Stat_distr\PLLOTOS00025.csv'
    dane = csv_to_list(path, [3]+range(5,13))
    print "##########################"
    for row in dane:
        print row
    conn = sqlite3.connect('example.db')
    c = conn.cursor()

    c.execute('''
              CREATE TABLE kursy
              (id INTEGER PRIMARY KEY AUTOINCREMENT,
              nazwa varchar(50) NOT NULL,
              kurs REAL)
              ''')

    for row in dane[1:]:
        ins = "INSERT INTO kursy (nazwa, kurs) VALUES('%s', %f)"
        print ins % (row[0], float(row[1].replace(',','.')))
        conn.execute(ins % (row[0], float(row[1].replace(',','.'))) )
    conn.commit()

    conn.close()
