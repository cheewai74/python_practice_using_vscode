product = {
    "description": "WCG E-Book",
    "price": 2.75,
    "sold": 1500,
    "stock": 5700
}


def sell(p):
    update = {"sold": p.get("sold", 0) + 1, "stock": p.get("stock") - 1}
    p.update(update)


"""
https://www.geeksforgeeks.org/join-function-python/

The join() method is a string method and returns a string in 
which the elements of sequence have been joined by str separator.

Syntax:

string_name.join(iterable) 

string_name: It is the name of string in which
             joined elements of iterable will be
             stored
"""


def print_product(p):
    print(", ".join(["{}: {}".format(str(k), str(product[k])) for k in sorted(p.keys())]))


print_product(product)
for i in range(0, 100):
    sell(product)
    print_product(product)

