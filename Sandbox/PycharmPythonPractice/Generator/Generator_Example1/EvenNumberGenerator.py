

import collections

# function approach
def even_integers_function(n):
    result = []
    for i in range(n):
        if i % 2 == 0:
            result.append(i)
    return result

# generator approach
def even_integers_generator(n):
    for i in range(n):
        if i % 2 == 0:
            yield i

#list comprehension
#newlist = [item.upper() for item in collections]

# generator expression
#(item.upper() for item in collections)

print(even_integers_function(20))

print(list(even_integers_generator(20)))  # Use list to see generator object

name_list = ['Adam', 'Anne', 'Barry', 'Barry', 'Brianne', 'Charlie', 'Cassandra', 'David', 'Dana']

#Converts names to uppercase
uppercase_names = (name.upper() for name in name_list)
reverse_uppercase = (name[::-1] for name in (name.upper() for name in name_list))
print(name_list)
print(list(uppercase_names)) # Use list to see generator object
print(list(reverse_uppercase))