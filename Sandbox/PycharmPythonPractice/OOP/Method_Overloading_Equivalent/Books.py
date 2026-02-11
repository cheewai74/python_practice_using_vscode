"""
If we don’t include the __add__ function, we will get an error where we won’t be able to add two objects.
So, operator overloading will help us in adding two or more objects depending upon the functionality
of __add__ function here.
"""
class Books:
    def __init__(self, price):
        self.mrp = price

    def __add__(self, book):
        return self.mrp + book.mrp

maths = Books(250)
science = Books(300)
print("Total Cost:", (maths + science))