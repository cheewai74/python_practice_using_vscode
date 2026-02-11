def myfunc(a, b):
    return a + b

funcs = [myfunc]
print(funcs[0])

print(funcs[0](2, 3))

# Function argument unpacking

def myfuncs(a, b, c):
    print(a, b, c)


tuple_vec = (1, 0, 1)
dict_vec = {'x': 1, 'y': 0, 'z': 1}

print(**dict_vec)
print(myfuncs(*tuple_vec))



