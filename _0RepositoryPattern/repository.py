# -*- coding: utf-8 -*-

import sqlite3
from datetime import datetime

#
# Ścieżka połączenia z bazą danych
#
db_path = 'invoice.db'

#
# Wyjątek używany w repozytorium
#
class RepositoryException(Exception):
    def __init__(self, message, *errors):
        Exception.__init__(self, message)
        self.errors = errors

#
# Model danych
#
class Invoice():
    """Model pojedynczej faktury
    """
    def __init__(self, id, date= datetime.now(), invitems=[]):
        self.id = id
        self.date = date
        self.invitems = invitems
        self.amount = sum([item.amount*item.qty for item in self.invitems])

    def __repr__(self):
        return "<Invoice(id='%s', date='%s', amount='%s', items='%s')>" % (
                    self.id, self.date, str(self.amount), str(self.invitems)
                )


class InvItem():
    """Model pozycji na fakturze. Występuje tylko wewnątrz obiektu Invoice.
    """
    def __init__(self, name, amount, qty):
        self.name = name
        self.amount = amount
        self.qty = qty

    def __repr__(self):
        return "<InvItem(name='%s', amount='%s', qty='%s')>" % (
                    self.name, str(self.amount), str(self.qty)
                )


#
# Klasa bazowa repozytorium
#
class Repository():
    def __init__(self):
        try:
            self.conn = self.get_connection()
        except Exception as e:
            raise RepositoryException('GET CONNECTION:', *e.args)
        self._complete = False

    # wejście do with ... as ...
    def __enter__(self):
        return self

    # wyjście z with ... as ...
    def __exit__(self, type_, value, traceback):
        self.close()

    def complete(self):
        self._complete = True

    def get_connection(self):
        return sqlite3.connect(db_path)

    def close(self):
        if self.conn:
            try:
                if self._complete:
                    self.conn.commit()
                else:
                    self.conn.rollback()
            except Exception as e:
                raise RepositoryException(*e.args)
            finally:
                try:
                    self.conn.close()
                except Exception as e:
                    raise RepositoryException(*e.args)

#
# repozytorium obiektow typu Invoice
#
class InvoiceRepository(Repository):

    def add(self, invoice):
        """Metoda dodaje pojedynczą fakturę do bazy danych,
        wraz ze wszystkimi jej pozycjami.
        """
        try:
            c = self.conn.cursor()
            # zapisz nagłowek faktury
            amount = sum([item.amount*item.qty for item in invoice.invitems])
            c.execute('INSERT INTO Invoice (id, inv_date, amount) VALUES(?, ?, ?)',
                        (invoice.id, str(invoice.date), invoice.amount)
                    )
            # zapisz pozycje faktury
            if invoice.invitems:
                for invitem in invoice.invitems:
                    try:
                        c.execute('INSERT INTO InvItems (name, amount, qty, invoice_id) VALUES(?,?,?,?)',
                                        (invitem.name, invitem.amount, invitem.qty, invoice.id)
                                )
                    except Exception as e:
                        #print "item add error:", e
                        raise RepositoryException('error adding invoice item: %s, to invoice: %s' %
                                                    (str(invitem), str(invoice.id))
                                                )
        except Exception as e:
            #print "invoice add error:", e
            raise RepositoryException('error adding invoice %s' % str(invoice))

    def delete(self, invoice):
        """Metoda usuwa pojedynczą fakturę z bazy danych,
        wraz ze wszystkimi jej pozycjami.
        """
        try:
            c = self.conn.cursor()
            # usuń pozycje
            c.execute('DELETE FROM InvItems WHERE invoice_id=?', (invoice.id,))
            # usuń nagłowek
            c.execute('DELETE FROM Invoice WHERE id=?', (invoice.id,))

        except Exception as e:
            #print "invoice delete error:", e
            raise RepositoryException('error deleting invoice %s' % str(invoice))

    def getById(self, id):
        """Get invoice by id
        """
        try:
            c = self.conn.cursor()
            c.execute("SELECT * FROM Invoice WHERE id=?", (id,))
            inv_row = c.fetchone()
            invoice = Invoice(id=id)
            if inv_row == None:
                invoice=None
            else:
                invoice.date = inv_row[1]
                invoice.amount = inv_row[2]
                c.execute("SELECT * FROM InvItems WHERE invoice_id=? order by name", (id,))
                inv_items_rows = c.fetchall()
                items_list = []
                for item_row in inv_items_rows:
                    item = InvItem(name=item_row[0], amount=item_row[1], qty=item_row[2])
                    items_list.append(item)
                invoice.invitems=items_list
        except Exception as e:
            #print "invoice getById error:", e
            raise RepositoryException('error getting by id invoice_id: %s' % str(id))
        return invoice

    def update(self, invoice):
        """Metoda uaktualnia pojedynczą fakturę w bazie danych,
        wraz ze wszystkimi jej pozycjami.
        """
        try:
            # pobierz z bazy fakturę
            inv_oryg = self.getById(invoice.id)
            if inv_oryg != None:
                # faktura jest w bazie: usuń ją
                self.delete(invoice)
            self.add(invoice)

        except Exception as e:
            #print "invoice update error:", e
            raise RepositoryException('error updating invoice %s' % str(invoice))



if __name__ == '__main__':
    try:
        with InvoiceRepository() as invoice_repository:
            invoice_repository.add(
                Invoice(id = 1, date = datetime.now(),
                        invitems = [
                            InvItem(name = "jablko",   amount = 0.30, qty = 10),
                            InvItem(name = "banan",    amount = 0.50, qty = 3),
                            InvItem(name = "gruszka",  amount = 0.40, qty = 5),
                        ]
                    )
                )
            invoice_repository.complete()
    except RepositoryException as e:
        print(e)

    print InvoiceRepository().getById(1)

    try:
        with InvoiceRepository() as invoice_repository:
            invoice_repository.update(
                Invoice(id = 1, date = datetime.now(),
                        invitems = [
                            InvItem(name = "mleko", amount = 1.30, qty = 2),
                            InvItem(name = "maslo", amount = 1.50, qty = 3),
                            InvItem(name = "ser",   amount = 1.40, qty = 4),
                        ]
                    )
                )
            invoice_repository.complete()
    except RepositoryException as e:
        print(e)

    print InvoiceRepository().getById(1)

    # try:
    #     with InvoiceRepository() as invoice_repository:
    #         invoice_repository.delete( Invoice(id = 1) )
    #         invoice_repository.complete()
    # except RepositoryException as e:
    #     print(e)
