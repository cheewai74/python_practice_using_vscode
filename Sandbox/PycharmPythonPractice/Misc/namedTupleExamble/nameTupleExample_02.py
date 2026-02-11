from collections import namedtuple

# Declaring namedtuple()
Student = namedtuple('Student', ['name','age','DOB'])

# Adding values
S = Student('John',48,20111974)

# Access using index
print("The student age using index is ", end="")
print(S[1])

# Access using name
print("The Student name using keyname is : ", end="")
print(S.name)

# Access using getattr()
print(" The Student DOB using getattr() is : ", end="")
print(getattr(S,'DOB'))
