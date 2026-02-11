products = ['apple', 'orange', 'sugarcane']
price = [3, 5, 1.5]
cost = [2, 2, 0.5]

for prod, p, c in zip(products, price, cost):
    print(f'The profit of a box of {prod} is ${p-c}!')