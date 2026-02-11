"""
    a = [5, 10, 15, 20]
    b = [5, 10, 15, 20]

    for it in range(0, len(a)):
        a[it] += b[it]

    Using zip() iterator to combine both of our list into one
    interator and instead loop through both of our lists as the
    same time

"""

a = [5, 10, 15, 20]
b = [5, 10, 15, 20]
empty=[]

for ai, bi in zip(a, b):
    z = ai + bi
    empty.append(z)

print(empty)

# Write out loop backward
# Advantage: speed and save memory
empty2 = [aii + bii for aii, bii in zip(a,b)]
print(empty2)