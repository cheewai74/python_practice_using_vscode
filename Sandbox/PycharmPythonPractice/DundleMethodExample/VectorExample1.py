class Vector():
    def __new__(cls, x, y):
        print("__new__ was invoked")
        instance = object.__new__(cls)
        return instance

    def __init__(self, x, y):
        print("__init__ was invoked")
        self.x = x
        self.y = y


vector1 = Vector(12, 8)


class Vector01:

    def __new__(cls, x, y):
        print("__new__ was invoked")
        instance = object.__new__(cls)
        return instance

    def __init__(self, x, y):
        print("__init__ was invoked")
        self.x = x
        self.y = y

    def __repr__(self):
        print("__repr__ was invoked")
        return f'Vector01({self.x}, {self.y})'


vector2 = Vector01(12, 8)
print(vector2)


class Vector02:

    def __new__(cls, x, y):
        print("__new__ was invoked")
        instance = object.__new__(cls)
        return instance

    def __init__(self, x, y):
        print("__init__ was invoked")
        self.x = x
        self.y = y

    def __repr__(self):
        print("__repr__ was invoked")
        return f'Vector02({self.x}, {self.y})'

    def __str__(self):
        print("__str__ was invoked")
        return f"{self.x}x + {self.y}y"


vector3 = Vector02(12, 8)
print(vector3)


class Vector03:

    def __new__(cls, x, y):
        print("__new__ was invoked")
        instance = object.__new__(cls)
        return instance

    def __init__(self, x, y):
        print("__init__ was invoked")
        self.x = x
        self.y = y

    def __repr__(self):
        print("__repr__ was invoked")
        return f'Vector03({self.x}, {self.y})'

    def __str__(self):
        print("__str__ was invoked")
        return f"{self.x}x + {self.y}y"

    """
        __len__()  is used to implement the built-in len()
    """
    def __len__(self):
        print("__len__ was invoked")
        return int((self.x * self.x + self.y * self.y) ** (1 / 2))

    """
         __call__() method defines what happens when an object is called. 
         You can use this to overcome the type restriction of the len() method and 
         return the magnitude of the vector in float.
    """

    def __call__(self):
        print("__call__ was invoked")
        print(f"Vector03({self.x}, {self.y}) was called.")
        return (self.x * self.x + self.y * self.y) ** (1 / 2)


vector4 = Vector03(15, 8)
print(vector4)