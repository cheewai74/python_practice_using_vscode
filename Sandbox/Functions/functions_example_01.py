print('hello','world')

other_print = print
other_print('This is just print with a new name')

num1 = 5
num2 = 7

def do_math(num1, num2=7):
    
    result = num1 * num2
    result = result + 10
    result = result / 1.5
    result = result - num1
    # print(result)
    return result
    
print(do_math(5, 7))
print(do_math(8, 10))
print(do_math(8))

import operator
print(operator.add(2,2))
print(operator.not_(True))
