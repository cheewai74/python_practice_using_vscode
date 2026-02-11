
def main():
    seq = range(11)
    from math import pi
    seq2 =[round(pi, i) for i in seq]
    print_list(seq)
    print_list(seq2)
    seq3 = {x: x**2 for x in seq}
    print(seq3)


def print_list(o):
    for x in o: print(x, end = ' ')
    print()

if __name__ == '__main__': main()
