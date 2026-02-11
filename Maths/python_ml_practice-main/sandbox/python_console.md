lambda:
f = lambda x,y : x+y
f(2,3)

lst = ['one', lambda x: x*x,3]
lst[1](4)

=============================================
class:

class MyClass:

    def f(self):
        return 'Hello World'

x=MyClass()
x.f()

E.g:

class MyPerson:

    def __init__(self, name, age):
        self.name = name
        self.age = age

        def printName(self):
        print("My name is " + self.name)

=============================================

# Using dtype to know the type of data the array is holding.

>>> import numpy as np
>>> list1 = [1,2,3,4,5]
>>> a = np.array(list1)
>>> print(a)
[1 2 3 4 5]
>>> print(a.shape)
(5,)
>>> print(a.dtype)
int32