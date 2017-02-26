# -*- coding: utf-8 -*-

import repository
import sqlite3
import unittest

db_path = 'invoice.db'

class RepositoryTest(unittest.TestCase):

    def setUp(self):
        conn = sqlite3.connect(db_path)
        c = conn.cursor()
        c.execute('DELETE FROM InvItems')
        c.execute('DELETE FROM Invoice')
        c.execute('''INSERT INTO Invoice (id, inv_date, amount) VALUES(1, '2016-01-01', 30)''')
        c.execute('''INSERT INTO InvItems (name, amount, qty, invoice_id) VALUES('mleko',5,4,1)''')
        c.execute('''INSERT INTO InvItems (name, amount, qty, invoice_id) VALUES('maslo',5,2,1)''')
        conn.commit()
        conn.close()

    def tearDown(self):
        conn = sqlite3.connect(db_path)
        c = conn.cursor()
        c.execute('DELETE FROM InvItems')
        c.execute('DELETE FROM Invoice')
        conn.commit()
        conn.close()

    def testGetByIdInstance(self):
        invoice = repository.InvoiceRepository().getById(1)
        self.assertIsInstance(invoice, repository.Invoice, "Objekt nie jest klasy Invoice")

    def testGetByIdNotFound(self):
        self.assertEqual(repository.InvoiceRepository().getById(22),
                None, "Powinno wyjść None")

    def testGetByIdInvitemsLen(self):
        self.assertEqual(len(repository.InvoiceRepository().getById(1).invitems),
                3, "Powinno wyjść 2")

    def testDeleteNotFound(self):
        self.assertRaises(repository.RepositoryException,
                repository.InvoiceRepository().delete, 22)



if __name__ == "__main__":
    unittest.main()
