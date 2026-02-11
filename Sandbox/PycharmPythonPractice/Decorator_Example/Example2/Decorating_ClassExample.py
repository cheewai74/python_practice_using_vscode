"""
    Python decorators are used for decorating class methods,

    @property is used to create property attributes that can only be accessed
    through its getter, setter, and deleter methods.

    @staticmethod and @classmethod are used to define class methods that are not connected
    to particular instances of the class.

    @staticmethod don’t require an argument.
    @classmethod take the class as an argument.

"""

class Account:

    def __init__(self, balance):
        self._balance = balance

    @property
    def balance(self):
        """Gets balance"""
        return self._balance

    @balance.setter
    def balance(self, value):
        """Set balance, raise error if negative"""
        if value >= 0:
            self._balance = value
        else:
            raise ValueError("balance must be positive")

    @classmethod
    def new_account(cls):
        """Returns a new account with 100.00 balance"""
        return cls(100.00)

    @staticmethod
    def interest():
        """The interest rate"""
        return 5.25


acc = Account(39825.75)
print(acc.balance)
acc.balance = 98621.75
print(acc.balance)

# testing if the setter is being used
try:
    acc.balance = -354
except:
    print("Setter method is being used")
acc2 = Account.new_account()
print(acc2.balance)
print(f"Calling static method using class: {Account.interest()}, using instance {acc.interest()}")