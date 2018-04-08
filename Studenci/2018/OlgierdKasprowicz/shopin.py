#!/usr/bin/env python3

SAMPLE_STOCK = {
    "a": {"price": 5},
    "b": {"price": 7},
    "c": {"price": 2},
}

SAMPLE_SHOPPING_LIST = ['a', 'b', 'd', 'e', 'f']

class InventoryMiss(Exception):
    def __init__(self, missing_items):
        self.missing_items = missing_items
        super().__init__()

    def __str__(self):
        return "There following items are missing from stock: {}".format(", ".join(self.missing_items))


def generate_aquisiton_list(shopping_list, stock):
    missing_items = set(shopping_list).difference(set(stock.keys()))

    if missing_items:
        raise InventoryMiss(missing_items)

    return {item: stock[item]["price"] for item in shopping_list}


def test_inventory_ok():
    assert generate_aquisiton_list(
        shopping_list=['a', 'd'],
        stock= {'a': {'price':5}, 'b': {'price':3}, 'c': {'price':6}, 'd': {'price': 7}}) == {'a': 5, 'd': 7}


def test_inventory_missing():
    try:
        generate_aquisiton_list(
            shopping_list=['a', 'e', 'f', 'd'],
            stock= {'a': {'price':5}, 'b': {'price':3}, 'c': {'price':6}, 'd': {'price': 7}            })
    except InventoryMiss as exception:
        assert exception.missing_items == {'f', 'e'}


def main():
    print(generate_aquisiton_list(SAMPLE_SHOPPING_LIST, SAMPLE_STOCK))


if __name__ == "__main__":
    main()
