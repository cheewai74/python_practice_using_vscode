from itertools import zip_longest

id = [1,2]
leaders = ["Elon Mask", "Tim Cook","Bill Gates", "Jack Ma"]
record = zip_longest(id, leaders)

print(list(record))