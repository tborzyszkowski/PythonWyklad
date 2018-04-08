def list_t (product, l_goods):

    products_with_price = {}
    for items in l_goods:
        products_with_price.update({items:0})
    for keys, values in product.items():
        products_with_price.update({keys:values})

    return products_with_price




product = {"papryka":1.00, "czipsy":2.50}
l_goods = ["papryka", "cebula", "czosnek"]

a = list_t(product, l_goods)
print a
