"""

python -m unittest test_calculator.TestCalculator
python -m unittest -f test_calculator.py (Test are stopped after failure)
python -m unittest -v test_calculator.py ()
python -m unittest test_calculator.TestCalculator.test_add (Execute 1 method)
python -m unittest test_calculator.py test_calculator2.py test_calculator3.py
python -m unittest -h

"""
import unittest
import calculator


class TestCalculator_01(unittest.TestCase):

    def setUp(self):
        self.calc = calculator.Calculator(5, 1)
        print('setUp method')

    def tearDown(self):
        print('tearDown method')

    def test_add(self):
        self.assertEqual(self.calc.add(), 6)
        self.calc.first = 8
        self.calc.second = 2
        self.assertEqual(self.calc.add(), 10)
        print('test_add method')

    def test_subtract(self):
        self.assertEqual(self.calc.subtract(), 4)
        self.calc.first = 8
        self.calc.second = 2
        self.assertEqual(self.calc.subtract(), 6)
        print('test_subtract method')


if __name__ == '__main__':
    unittest.main()
