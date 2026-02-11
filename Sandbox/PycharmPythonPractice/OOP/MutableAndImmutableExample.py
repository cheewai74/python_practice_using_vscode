"""
    Mutable Example: List
"""

closet = ['shirt','hat','pants','jacket','socks']
print(closet)
a = id(closet)
print(a)
closet.remove('hat')
print(closet)
b = id(closet)
print(b)
if a == b:
    print("Mutable")
else:
    print("Immutable")

"""
    Immutable Example: String
"""

words = "You are wearing that"
print(words)
a = id(words)
print(a)
words = words + ", because you look great"
b = id(words)
if a == b:
    print("Mutable")
else:
    print("Immutable")



