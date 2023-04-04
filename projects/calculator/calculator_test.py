import unittest
from projects.calculator.calculator import Calculator

class TestCalculator(unittest.TestCase):
    def setUp(self):
        self.calc = Calculator()

    def test_add(self):
        self.assertEqual(self.calc.add(2, 7), 9)

    def test_subtract(self):
        self.assertEqual(self.calc.subtract(7, 2), 5)

    def test_multiply(self):
        self.assertEqual(self.calc.multiply(3, 5), 15)

    def test_divide(self):
        self.assertEqual(self.calc.divide(15, 3), 5)

if __name__ == '__main__':
    unittest.main()
    