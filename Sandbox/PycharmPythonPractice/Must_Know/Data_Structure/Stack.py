class Stack:

    def __init__(self):
        self.items=[]

    def push(self, item):
        """
        Accepts an item as a parameter and appends it to the end of the list. Return Nothing


        """
        self.items.append(item)

    def pop(self):
        """
        Removes and returns the last item for the list, which is also the
        top item of the stack

        The runtime here is constant time, becos all it does is index to the
        last item of the list
        """
        if self.items:
            return self.items.pop()

        return None

    def peek(self):
        """
        This method returns the last item in the list, which is also theitem
        at the top of the stack.
        
        This method runs in constant time bcos indexing into a list is done
        in constant time.
        """
        if self.items:
            return self.items[-1]
        return None

    def size(self):
        """
        This method returns the length of the list that is representing the stack.

        This method runs in constant time becos finding the length of the list
        also happens in constant time.
        """

        return len(self.items)

    def is_empty(self):
        """
        This method returns a Boolean value describing whether or not the
        Stack is empty

        Testing for equality happens in constant time
        """
        return self.items == []

my_stack = Stack()
my_stack.pop()
print(my_stack.is_empty())
print(my_stack.size())
my_stack.push('apple')
print(my_stack.is_empty())
my_stack.peek()
print(my_stack.size())
print(my_stack.items)
my_stack.push('banana')
print(my_stack.items)
my_stack.push('carrot')
print(my_stack.items)
my_stack.pop()
print(my_stack.items)
my_stack.peek()
print(my_stack.items)


