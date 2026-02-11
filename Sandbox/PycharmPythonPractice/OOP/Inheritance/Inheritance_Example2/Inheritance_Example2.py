"""
From Udemy Object Oriented Programming Course
"""
class Person:

    def __init__(self, name, age, address, phone):
        self.name = name
        self.age = age
        self.address = address
        self.phone = phone

    def greet(self):
        print("I am ", self.name)

    def is_adult(self):
        if self.age > 18:
            return True
        else:
            return False

    def contact_details(self):
        print(self.address, self.phone)


class Employee(Person):

    def __init__(self, name, age, address, phone, salary,
                 office_address, office_phone):
        # self.name = name;
        # self.age = age;
        # self.address = address
        # self.phone = phone

        # Person.__init__(self, name, age, address, phone) # Call the Base Class
        super().__init__(name, age, address, phone)  # call the Base Class

        self.salary = salary
        self.office_address = office_address
        self.office_phone = office_phone

    def calculate_tax(self):
        if self.salary < 5000:
            return 0
        else:
            return self.salary * 0.05

    def contact_details(self):

        # Person.contact_details(self) # call the Base Class
        super().contact_details()  # call the Base Class

        print(self.office_address, self.office_phone)


emp = Employee("Tim", 18, "Queenstown Blk 45", "778999", 8000, "Hong Kong Drive", "1234567")
print(emp.name)
print(emp.age)
print(emp.greet())
print(emp.contact_details())
print(emp.is_adult())
print(isinstance(emp, Employee))
print(isinstance(emp, Person))
print(issubclass(Employee, Person))
print(issubclass(Person, object))

print(emp.salary)
print(emp.calculate_tax())
