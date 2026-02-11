"""
It can behave as a single argument, double argument, and no argument functio
"""
class Book_Food:
    def book(self,lunch=None, dinner=None):
        if lunch and dinner:
            print("Lunch & Dinner Booked")
        elif lunch:
            print("Lunch Booked")
        elif dinner:
            print("Dinner Booked")
        else:
            print("No food item booked")

obj = Book_Food()
print(obj.book())
print(obj.book(lunch=1))
print(obj.book(lunch=1, dinner=1))
