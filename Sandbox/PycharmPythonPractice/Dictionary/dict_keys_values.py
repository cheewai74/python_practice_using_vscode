def print_dict(dictionary):
    ks = list(dictionary.keys())
    vs = list(dictionary.values())
    for i in range(0, len(ks)):
        k = ks[i]
        v = vs[i]
        print("{}: {}".format(str(k), str(v)))


example = {
    "name": "Sebastian",
    "last_name": "Vinci",
    "age": 21
}

print_dict(example)