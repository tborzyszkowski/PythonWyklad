# -*- coding: utf-8 -*-

import sqlite3


db_path = 'invoice.db'
conn = sqlite3.connect(db_path)

c = conn.cursor()
#
# Tabele
#
c.execute('''
          CREATE TABLE Invoice
          ( id INTEGER PRIMARY KEY,
            inv_date DATE NOT NULL,
            amount NUMERIC NOT NULL
          )
          ''')
c.execute('''
          CREATE TABLE InvItems
          ( name VARCHAR(100),
            amount NUMERIC NOT NULL,
            qty INTEGER NOT NULL,
            invoice_id INTEGER,
           FOREIGN KEY(invoice_id) REFERENCES Invoice(id),
           PRIMARY KEY (name, invoice_id))
          ''')
