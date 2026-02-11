from time import time

def diagnostics(f):
    def wrapper(*args, **kwargs):
        '''
        In Python, functions have attributes, just as other objects do. You can use the
        __fname__ attribute to get the name of the function at the time it was defined.
        print(f.__name__)
        '''

        print('Executed', f.__name__, 'at', time())
        value = f(*args, **kwargs)
        print('Exited ', f.__name__, 'at', time())
        print('Arguments:', args)
        print('Value returned:', value, '\n')
        return value
    return wrapper

@diagnostics
def print_nums():
    for i in range(4):
        print(i, end='\t')
        print()

@diagnostics
def calc_hypotenuse(a, b):
    return ((a*a + b*b) ** 0.5)

print_nums()
print (calc_hypotenuse(3, 4))