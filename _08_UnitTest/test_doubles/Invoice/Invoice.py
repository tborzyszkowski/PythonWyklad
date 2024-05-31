from abc import ABC


class Invoice(ABC):
    def __init__(self, number=None, customer=None, items=None):
        self.__number = number
        self.__customer = customer
        self.__items = items

    def __eq__(self, other):
        if isinstance(other, Invoice):
            return self.number == other.number
        else:
            return False

    def __hash__(self):
        return hash(self.number)

    def __repr__(self):
        return f"Invoice({self.number}, {self.customer}, {self.items})"

    @property
    def number(self):
        return self.__number

    @number.setter
    def number(self, value):
        self.__number = value

    @property
    def customer(self):
        return self.__customer

    @customer.setter
    def customer(self, value):
        self.__customer = value

    @property
    def items(self):
        return self.__items

    @items.setter
    def items(self, value):
        self.__items = value

