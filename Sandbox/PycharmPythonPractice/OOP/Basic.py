
class MyClass:
    MyVar = 0 # Class Variable

    def SayHello():
        print("Hello")

    """
    Concept:
    1. Use instance methods to manipulate the data that class manages 
    2. Can't Use instance method until you instantiate an object from the class
    """
    def SayHelloWord(self):
        print("Hello World")

MyInstance = MyClass() # Create an instance of MyClass named MyInstance
print(MyInstance.__class__)
print(dir(MyInstance)) # Using dir to determine which build-in attrib are present
print(MyClass.SayHello())

print (MyInstance.SayHelloWord())