def addition(*args):
    result = 0
    for arg in args:
        result += arg
    return result

print(addition(5, 10, 15, 20, 25))
print(addition(1, 2, 3, 4, 5))


my_nums = [5, 10, 15, 20, 25]

# unpack the numbers
print(addition(*my_nums))