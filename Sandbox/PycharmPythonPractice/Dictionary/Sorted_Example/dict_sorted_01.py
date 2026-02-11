"""
    How to sort a Python dict by value
"""
import operator


xs = {'a': 4, 'b': 5, 'c': 6, 'd': 7}


print(sorted(xs.items(), key=lambda x: x[1]))

print(sorted(xs.items(), key=operator.itemgetter(1)))

