from Employee import*;

"""
    Inheritance Example
"""
class Manager(Employee):

    def give_raise(self):
        self.salary = self.salary * 1.10

mgr1 = Manager(101, 75000)
print(mgr1.salary)
mgr1.give_raise()
print(mgr1.salary)

