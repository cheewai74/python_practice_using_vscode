"""

    Output:
            [’name’, ’age’]
"""

my_dict = {
    "name": "Sebastian",
    "age": 21
}


def keys_01(dictionary):
    return [k for k in dictionary]


def keys_02(dictionary):
    result = [k for k in dictionary]
    # result.append("break the program plz")
    if len(result) != len(dictionary):
        raise Exception('expected {} keys. got {}'.format(len(dictionary), len(result)))
    return result


print(str(keys_01(my_dict)))
print(str(keys_02(my_dict)))