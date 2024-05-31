from abc import ABC
from Invoice import Invoice


class Shop(ABC):
    def __init__(self, repository=None):
        self.__invoice_repository = repository

    def buy(self, customer, items_list):
        invoice = Invoice(number=self.invoice_repository.get_next_number(), customer=customer, items=items_list)
        self.invoice_repository.add(invoice)
        return invoice

    def returning_goods(self, invoice):
        if self.invoice_repository.find_by_number(invoice.number):
            self.invoice_repository.delete(invoice)
            return True
        else:
            return False

    @property
    def invoice_repository(self):
        return self.__invoice_repository
