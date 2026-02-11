from Manager import *;
from Director import *;
from Employee import *;

def bulk_raise(list_of_emps):
    for emp in list_of_emps:
        emp.give_raise()

emp_a = Employee(101, 45000)
emp_b = Manager(103, 60000)
emp_c = Director(105, 70000)
list_of_emps = [emp_a, emp_b, emp_c]

bulk_raise(list_of_emps)
print(emp_a.salary)
print(emp_b.salary)
print(emp_c.salary)