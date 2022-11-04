from collections import OrderedDict, Counter

# Remembers the order the keys are added!
x = OrderedDict(a=1, b=2, c=3)
print(x)

#Counts the frequency of each character
y = Counter("Hello World!")
print(y)