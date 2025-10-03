from simple_calculator import SimpleCalculator
import unittest

class TestSimpleCalculator(unittest.TestCase):

    def setUp(self):
        """Set up the SimpleCalculator instance before each test."""
        self.calc = SimpleCalculator()

    def test_add(self):
        self.assertEqual(self.calc.add(4, 4), 8)
        self.assertEqual(self.calc.add(0, 4), 4)
        self.assertEqual(self.calc.add(5, 1), 6)

    def test_substrate(self):
        self.assertEqual(self.calc.subtract(4, 0), 4)
        self.assertEqual(self.calc.subtract(4, 4), 0) 
        self.assertEqual(self.calc.subtract(5, 4), 1) 

    def test_multiply(self):
        self.assertEqual(self.calc.multiply(0, 4), 0)
        self.assertEqual(self.calc.multiply(4, 4), 16) 
        self.assertEqual(self.calc.multiply(5, 4), 20) 

    def test_divide(self):
        self.assertEqual(self.calc.divide(4, 4), 1)
        self.assertEqual(self.calc.divide(16, 4), 4)  
        self.assertEqual(self.calc.divide(4, 0), "Error: Cannot divide by zero.")                