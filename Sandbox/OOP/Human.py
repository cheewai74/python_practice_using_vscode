class Human:
    
    # The __init__ method: This special method is called the constructor and
    # is used to initialize the object's attributes.
    # The self parameter refers to the instance of the class being created.
    
    def __init__(self, name, age):
        self.name = name
        self.age = age
        
    def say_hello(self):
        print("Hello, my name is ", self.name)
        
    def get_age(self):
        return self.age
    
human1 = Human("Tom", 25)
human2 = Human("Kate", 48)

human1.say_hello()
print(human2.get_age())