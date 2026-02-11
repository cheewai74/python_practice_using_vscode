def add(x, y):
    return x + y

print(add(5,5))

"""
A lambda operator or lambda function is used for creating small, 
one-time, anonymous function objects in Python.

Basic Syntax
lambda arguments : expression
"""
add_01 = lambda x, y: x+y
print(add_01(6, 7))