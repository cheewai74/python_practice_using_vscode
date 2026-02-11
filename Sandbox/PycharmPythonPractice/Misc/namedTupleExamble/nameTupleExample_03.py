import collections

# Declaring namedtuple()
Student = collections.namedtuple('Student',['name', 'age','DOB'])

# Adding Student
S = Student('John',48,20111974)

# Initializing iterable
Ii = ['John',48,4011974]

# Initializing dict
di = { 'name': 'John', 'age': 48, 'DOB': 24041972}

"""
_make() :- This function is used to return a namedtuple() 
           from the iterable passed as argument.

"""
# using _make() to return namedtuple()
print("The namedtuple instance using iterable is : ")
print(Student._make(Ii))

# using _asdict() to return an OrderedDict()
print("The OrderedDict instance using namedtuple is : ")
print(S._asdict())

# using ** operator to return namedtuple from dictionary
print("The namedtuple instance from dict is  : ")
print(Student(**di))

# using _fields to display all the keynames of namedtuple()
print ("All the fields of students are : ")
print(Student._fields)

# using _replace() to change the attribute values of namedtuple
print ("The modified namedtuple is : ")
print(S._replace(name= 'Tommy'))