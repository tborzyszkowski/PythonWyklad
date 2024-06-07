import unittest
from unittest.mock import Mock
from InvoiceRepository import InvoiceRepository
from Shop import Shop
from Invoice import Invoice


class ShopTests(unittest.TestCase):
    def test_while_buy_the_repository_add_should_be_called(self):
        spy_repository = Mock(InvoiceRepository)
        shop = Shop(spy_repository)
        shop.buy(customer="Jan", items_list=["cukierki"])
        spy_repository.add.assert_called_once()

    def test_while_returning_goods_the_repository_returns_false_when_not_find(self):
        stub_repository = Mock(InvoiceRepository)
        shop = Shop(stub_repository)
        stub_repository.find_by_number.return_value = None
        result = shop.returning_goods(Mock(Invoice))
        self.assertEqual(result, False)

    def test_while_returning_goods_the_repository_delete_should_be_called_when_find(self):
        spy_repository = Mock(InvoiceRepository)
        shop = Shop(spy_repository)
        spy_repository.find_by_number.return_value = Invoice()
        shop.returning_goods(Mock(Invoice))
        spy_repository.delete.assert_called_once()
