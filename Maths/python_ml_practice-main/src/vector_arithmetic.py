import numpy as np

a = np.array([20,40,60])
b = np.array([10,20,30])
c = np.array([5.10,15,20])
print(a+b)
print(a-b)
print(a/b)
print(a*b)

scalar=2
list_a = [10,11,12,13,14,15]
list_as_array = np.array(list_a)
print(list_a)
print(list_as_array)
print(scalar * list_a)
print(scalar * list_as_array)

e = np.array([1,2,3,4,5])
f = np.array([6,7,8,9,10])
print(np.dot(e,f))

g = np.array([11,12,13,14,15])
print(np.dot(f,e))

first_result=np.dot(e,f+g)
print(first_result)

second_result = np.dot(e,f) + np.dot(e,g)
print(second_result)
