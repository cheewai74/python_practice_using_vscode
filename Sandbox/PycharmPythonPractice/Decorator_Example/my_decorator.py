def my_decorator(func):
    '''Decorator function'''
    def wrapper():
        '''Return string F-I-B-O-N-A-C-C-I'''
        return 'F-I-B-O-N-A-C-C-I'
    return wrapper

def pfib():
    '''Return fibonacci'''
    return 'Fibonacci'

print(pfib())
pfib = my_decorator(pfib)
print(pfib())

'''
@my_decorator
def pfib():
    return Fibonacci
    
equivalent to 
pfib = my_decorator(pfib)

'''
@my_decorator
def _pfib():
    '''Return fibonacci'''
    return 'Fibonacci'

print(_pfib())
print(_pfib)

'''
    Decorator Template
    
    def my_decorator(func):
        def wrapper():
            # Do something before
            result = func()
            # Do something after
            return result
        return wrapper
        
    @my_decorator
    def func():
        pass

'''