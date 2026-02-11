# this code is in the calculator.py file
import self as self


class Calculator:

    def __init__(self, first, second):
        self.first = first
        self.second = second

    def add(a, b):
        """ Addition """
        return a + b

    def add(self):
        return self.first + self.second


    def multiply(a, b):
        """ Multiplication """
        return a * b

    def multiply(self):
        """ Multiply """
        return self.first * self.second

    def subtract(a, b):
        """ Subtraction """
        return a - b

    def subtract(self):
        """ Subtraction """
        return self.first - self.second

    def divide(self):
        """ Division """
        if self.second == 0:
            raise ValueError('Can not divide by zero!')
        return self.first / self.second

    def divide(x, y):
        """ Division """
        if y == 0:
            raise ValueError('Can not divide by zero!')
        return x / y
