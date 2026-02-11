"""
    This method returns a list of tuples containing every key-value pair
    in the dictionary as ({"a":1, "b":2}.items() =>
    [("a", 1), ("b", 2)]).

"""


def print_dict(dictionary):
    for k, v in dictionary.items():
        print("{}: {}".format(str(k), str(v)))


example = {
    "name": "Sebastian",
    "last_name": "Vinci",
    "age": 21
}


print_dict(example)

