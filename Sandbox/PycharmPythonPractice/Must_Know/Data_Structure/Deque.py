class Deque:

    def __init__(self):
        self.items = []

    def add_rear(self, item):
        """
        Takes an item as a parameter and appends that item to the end
        of the list that is representing the Deque.

        The runtime is constant, bcos appending to the end of a list
        happens in constant time.
        """
        self.items.append(item)

    def add_front(self, item):
        """
        Takes an item as a parameter and inserts it into the 0th index
        of the list that is representing the Deque.

        The runtime is linear, or O(n), bcos everytime you insert into the
        front of a list, all the other items in the list need to shift one
        position to the right
        """
        self.items.insert(0, item)

    def remove_rear(self):
        """
        Removes and returns the last item of the list, which represents the
        rear of the Deque.

        The runtime is constant bcos all we're doing is indexing to the
        end of a list.
        """
        if self.items:
            return self.items.pop()
        return None

    def remove_front(self):
        """
        Removes and return the item in the 0th index of the list, which
        represents the front of the Deque

        The runtime is linear or O(n), bcos when we remove an item from the 0th index,
        all the other items have to shift from one index to the left
        """
        if self.items:
            return self.items.pop(0)
        return None

    def peek_rear(self):
        if self.items:
            return self.items[-1]
        return None

    def peek_front(self):
        if self.items:
            return self.items[0]
        return None

    def size(self):
        """
        Return the size of the Queue, which is represent by the length of the list.

        The runtime is O(1), or constant time, bcos we're only returning the length
        """

        return len(self.items)

    def is_empty(self):
        """
        Returns a Boolean value expressing whether or not the list r
        representing the Queue is empty

        runs in constant time, bcos it's only checking for equality
        """
        return self.items == []

my_d = Deque()
print(my_d.items)
my_d.add_front('apple')
print(my_d.items)
my_d.add_front('banana')
print(my_d.items)
print(my_d.peek_front())
my_d.add_rear('carrot')
print(my_d.items)
print(my_d.peek_rear())
my_d.remove_front()
print(my_d.items)
my_d.remove_rear()
print(my_d.items)
