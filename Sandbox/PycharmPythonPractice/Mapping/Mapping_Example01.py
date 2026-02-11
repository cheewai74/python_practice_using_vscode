"""
    Map method will take the function we would like to map as well as iterable
    as positional arguments in that order

    map(function_object, iterable1, iterable2,...)

    # Output
    [10, 15, 20, 25]
    [10, 15, 20, 25]
"""
data = [5, 10, 15, 20]

def add5(x):
    return (x+5)

newdata = map(add5,data)
print(list(newdata))

newdata2 = list(map(lambda x: x+5, data))
print(newdata2)
