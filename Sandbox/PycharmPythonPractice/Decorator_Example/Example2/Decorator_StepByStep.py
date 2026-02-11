"""

    def square(x):
        print(x*x)

    def cube(x):
        print(x*x*x)

    def quartic(x):
        print(x**4)

    power_two = square
    power_two(6)

    powers = [square, cube, quartic]
    powers[2](5)

"""


def decorator_function(func):

    ''' A function that accepts another function '''
    def wrapper():
        print('wrapping')
        func()
        print("done")

    return wrapper

def f():
    '''Example function '''
    print("function f called")

decorator = decorator_function(f)
print(decorator)
# The inner wrapper function is returned so it needs to be called
decorator()

"""
 The function  decorator_function is a decorator and can be used to wrap
 other functions using the @decorator_name syntax
"""
@decorator_function
def g():
    ''' Yet another useless example function '''
    print("function g called")

g()

"""
    Creating a Decorator for Functions with Arguments
    *args and **kwargs
"""

def decorator_arguments(func):

    def wrapper(*args, **kwargs):
        print("decorating")
        func(*args, **kwargs)
        print("done")

    return wrapper

@decorator_arguments
def add(a, b, c, d):
    print("Sum is {}".format(a + b + c + d))

add(10, 54, 13, 34)

def multiply(*outer_args, **outer_kwargs):
     def inner_function(func):
         def wrapper(*func_args, **func_kwargs):
             print(f"Times {outer_args[0]} is {outer_args[0] * func(*func_args, **func_kwargs)}")
         return wrapper
     return inner_function

@multiply(99)
def basically_an_input(n):
    print(f"Input number {n}")
    return n


basically_an_input(5)
