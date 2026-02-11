from functools import wraps

'''
Decorator Template With *args and **kwargs

def decorator(func):
    @wrap(func)
    def wrapper(*args, **kwargs):
        # Do somethng before
        result = func(*args, **kwargs)
        # Do something after
        return result
    return wrapper

@decorator
def func():
    pass

'''

def pfib(*args, **kwargs):
    print(args)
    print(kwargs)

def wrapper(*args, **kwargs):
    print("In wrapper: ")
    print(*args)
    pfib(*args, **kwargs)

print(wrapper(1,1,th=2))