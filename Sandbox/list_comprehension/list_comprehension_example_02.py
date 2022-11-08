numbers = [1, 2, 3, 4, 5, 6, 7]
evens = [x for x in numbers if x % 2 is 0]
odds = [x for x in numbers if x not in evens]
print(evens)
print(odds)