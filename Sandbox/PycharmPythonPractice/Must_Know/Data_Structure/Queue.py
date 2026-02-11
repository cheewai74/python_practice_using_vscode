class Queue:

    def __init__(self):
        self.items = []

    def enquene(self, item):
        """
        Takes in an item and inserts that item into the 0th index of the list
        that is representing the Queue.

        he runtime is O(n), or linear time, bcos inserting into the 0th index of a list
        forces all the other items in the list to move one index to the right.
        """
        self.items.insert(0, item)

    def dequene(self):
        """
        Returns and remove the front-most item at the Queue, which is
        represented by the last item in the list.

        The runtime is O(1), or constant time, becos indexing to the end of a
        list happens in constant time.
        """
        if self.items:
            return self.items.pop()
        return None

    def peek(self):
        """
        Returns the last item in the list. Which represents the front-most
        item in the Queue

        The runtime is constant bcos we're just indexing to the last item of the list
        and returning the value found there.
        """
        if self.items:
            return self.items[-1]
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

my_q = Queue()
my_q.enquene('apple')
print(my_q.items)
my_q.enquene('banana')
print(my_q.items)
print(my_q.dequene())
print(my_q.items)
print(my_q.dequene())
print(my_q.items)
print(my_q.dequene())
print(my_q.items)
print(my_q.peek())
print(my_q.peek())
print(my_q.size())
my_q.enquene('apple')
print(my_q.items)
my_q.enquene('banana')
print(my_q.size())
print(my_q.is_empty())
print(my_q.items)
print(my_q.peek())
print(my_q.size())
print(my_q.is_empty())
print(my_q.peek())
print(my_q.size())