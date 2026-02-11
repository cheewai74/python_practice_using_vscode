"""
    The in keyword is a tool Python provides to, in this case,
    check whether a key is present in a dictionary or not.

"""


def get(dictionary, key, default_value=None):
    if key in dictionary:
        return dictionary[key]
    else:
        return default_value


my_dict = {
"name": "Sebastian",
"age": 21
}

print(str(get(my_dict, "name", "Name was not present")))
print(str(get(my_dict, "age", "Age was not present")))
print(str(get(my_dict, "address", "Address was not present")))