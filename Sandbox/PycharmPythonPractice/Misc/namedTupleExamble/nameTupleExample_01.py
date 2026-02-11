
from collections import namedtuple

Car = namedtuple('Car', 'color mileage')

my_car = Car('red', 3812.4)
print(my_car.color)
print(my_car.mileage)
print(my_car)

try:
    my_car.color='blue'
except AttributeError:
    print('nametuples are immutable')
finally:
    print(my_car.color)