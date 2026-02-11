"""
    Remark:
    we defined an array xs and another one ys and ys is shorter than xs.

"""


def multiply(x, y):
    return x * y


def test_example1():
    xs = [1, 2, 3, 4, 5, 6, 7, 8]
    ys = [2, 3, 4, 5, 6, 7]

    # It does not accept only one array, but n instead
    map_object = map(multiply, xs, ys)

    # It does not return a list, but a map object,
    # but if you apply list to it, will become a list.

    result_list = list(map_object)
    print(str(result_list))


"""

    In real life, we often don’t want to define a function to pass it to a map, 
    as it probably will only be used there. Lambdas come to help.
    
"""


def test_example2():
    xs = [1, 2, 3, 4, 5, 6, 7, 8]
    ys = [2, 3, 4, 5, 6, 7]
    map_objects = map(lambda x, y: x * y, xs, ys)
    result_list = list(map_objects)
    print(str(result_list))


if __name__ == "__main__":

    test_example1()

    test_example2()