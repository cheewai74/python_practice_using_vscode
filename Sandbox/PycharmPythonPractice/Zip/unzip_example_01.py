# The trick is to use asterisk

record = [(1, 'Elon Mask'), (2, 'Tim Cook'), (3, 'Bill Gates'), (4, 'Jack Ma')]
id, leaders = zip(*record)
print(list(id))
print(list(leaders))