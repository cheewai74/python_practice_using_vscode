"""
Method	                                        What it checks

assertEqual(a, b)       	                    a == b
assertNotEqual(a, b)    	                    a != b
assertTrue(x)           	                    bool(x) is True
assertFalse(x)          	                    bool(x) is False
assertIsNone(x)         	                    x is None
assertIsNotNone(x)      	                    x is not None
assertGreater(a, b)     	                    a > b
assertLess(a, b)        	                    a < b
assertIsInstance(a, b)  	                    isinstance(a, b)
assertRaises(exception, function, arguments)	The function raises the exception when given the arguments

"""
import unittest
import calculator


class TestCalculator(unittest.TestCase):

    def test_add(self):
        self.assertEqual(calculator.add(6, 4), 10, 'Error when adding two positive numbers')
        self.assertEqual(calculator.add(6, -4), 2, 'Error when adding two positive numbers')
        self.assertEqual(calculator.add(-6, 4), -2, 'Error when adding two positive numbers')
        self.assertEqual(calculator.add(-6, -4), -10, 'Error when adding two positive numbers')

    def test_divide(self):
        with self.assertRaises(ValueError):
            calculator.divide(5,0)


"""
Command Line Equivalent:
python -m unittest
python -m unittest test_calculator
"""
if __name__ == '__main__':
    unittest.main()
