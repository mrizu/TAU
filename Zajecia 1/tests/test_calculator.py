from ..Calculator.calculator import Calculator
import unittest

calculator = Calculator()


class TestCalculator(unittest.TestCase):

    def test_add(self):
        calculator.add(3, 6)
        self.assertEqual(calculator.result, 9)

    def test_add_negative(self):
        calculator.add(-5, -6)
        self.assertEqual(calculator.result, -11)

    def test_subtract(self):
        calculator.subtract(10, 6)
        self.assertEqual(calculator.result, 4)

    def test_subtract_negative(self):
        calculator.subtract(-7, -8)
        self.assertEqual(calculator.result, 1)

    def test_multiply(self):
        calculator.multiply(7, 7)
        self.assertEqual(calculator.result, 49)

    def test_multiply_negative(self):
        calculator.multiply(-7, -7)
        self.assertEqual(calculator.result, 49)

    def test_multiply_one_negative(self):
        calculator.multiply(-7, 7)
        self.assertEqual(calculator.result, -49)

    def test_multiply_by_0(self):
        calculator.multiply(7, 0)
        self.assertEqual(calculator.result, 0)

    def test_divide(self):
        calculator.divide(12, 4)
        self.assertEqual(calculator.result, 3)

    def test_divide_by_0(self):
        self.assertRaises(ZeroDivisionError, calculator.divide, 12, 0)


