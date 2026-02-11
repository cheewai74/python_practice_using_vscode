try:
    1 / 0
except ZeroDivisionError as e:
    print(str(e) + ". But it is totally fine.")

# In order to throw an exception you should use the raise keyword:

x = 10
if x > 5:
    raise Exception('x should not exceed 5. The value of x was: {}'.format(x))

"""
    with statement in Python is used in exception handling to 
    make the code cleaner and much more readable
"""
try:
    with open('file.log') as file:
        read_data = file.read()
except:
    print('Could not open file.log')

"""    
    without using with statement
"""
file = open('file.log', 'r')
try:
    file.write('hello world')
finally:
    file.close()