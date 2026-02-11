from datetime import datetime
products = {
    1: {
        "id": 1,
        "name": "Python Book"
    },
    2: {
        "id": 2,
        "name": "JavaScript Book"
    },
    3: {
        "id": 3,
        "name": "HTML Book"
    }
}


prices = {
    1: [
        {
            "id": 1,
            "product_id": 1,
            "amount": 2.75,
            "date": datetime(2016, 2, 1, 11, 11, 17, 683987)
        },
        {
            "id": 4,
            "product_id": 1,
            "amount": 3.99,
            "date": datetime(2016, 2, 5, 11, 11, 17, 683987)
        }
    ],
    2: [
        {
            "id": 2,
            "product_id": 2,
            "amount": 1.10,
            "date": datetime(2015, 1, 5, 11, 11, 17, 683987)
        },
        {
            "id": 2,
            "product_id": 2,
            "amount": 1.99,
            "date": datetime(2015, 12, 5, 11, 11, 17, 683987)
        }
    ],
    3: [
        {
            "id": 3,
            "product_id": 3,
            "amount": 3,
            "date": datetime(2015, 12, 20, 11, 11, 17, 683987)
        }
    ]
}


def complete_product(product):
    if product is None:
        return None
    product_prices = prices.get(product.get("id"))
    if product_prices is None:
        return None
    else:
        p = product.copy()
        p["price"] = max(product_prices, key=lambda price: price.get("date")).copy()
    return p


def get_product(product_id):
    return complete_product(products.get(product_id))


def many_products(ids):
    return list(map(get_product, ids))


def all_products():
    return list(map(complete_product, products.values()))


if __name__ == "__main__":
    print("printing all...")
    ps = all_products()
    for p in ps:
        print(str(p))
    print("printing all, but by all ids...")
    ids = map(lambda p: p.get("id"), all_products())
    ps = many_products(ids)
    for p in ps:
        print(str(p))