# -*- coding: utf-8 -*-

import sqlite3
conn = sqlite3.connect('example.db')

c = conn.cursor()
#
# Tabele
#
c.execute('''
          CREATE TABLE person
          (id INTEGER PRIMARY KEY ASC, name varchar(250) NOT NULL)
          ''')
c.execute('''
          CREATE TABLE address
          (id INTEGER PRIMARY KEY ASC, street_name varchar(250),
          street_number varchar(250),
           post_code varchar(250) NOT NULL, person_id INTEGER NOT NULL,
           FOREIGN KEY(person_id) REFERENCES person(id))
          ''')
#
# Wstawianie
#
c.execute('''
          INSERT INTO person VALUES(1, 'pythoncentral')
          ''')
c.execute('''
          INSERT INTO address VALUES(1, 'python road', '1', '00000', 1)
          ''')

conn.commit()

#
# wybieranie danych
#

c.execute('SELECT * FROM person')
print c.fetchall()
c.execute('SELECT * FROM address')
print c.fetchall()

#
# usuń tabele
#
# c.execute('DROP TABLE address')
# c.execute('DROP TABLE person')

conn.close()

#################################
# Zadanie
# Na podstawie danych zgromadzinych w pliku PLLOTOS00025.csv
# zbubuj tabelę zawierającą dane dotyczące wycen społek giełdowych.
# Do tabeli tej dodaj wiersze zawierające wyceny z pliku PLLOTOS00025.csv
# Napisz zapytanie wypisujące maksymalne, minimalne i średnie wyceny.
