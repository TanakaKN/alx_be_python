from simple_calculator import SimpleCalculate
import unittest

class test_simple_calculator(unittest.TestCase):
    
    def test_add(self):
        self.assertEqual(SimpleCalculate.add(4, 4), 8)
        self.assertEqual(SimpleCalculate.add(0, 4), 4)
        self.assertEqual(SimpleCalculate.add(5, 1), 6)

    def test_substrate(self):
        self.assertEqual(SimpleCalculate.subtract(0, 4), 4)
        self.assertEqual(SimpleCalculate.subtract(4, 4), 0) 
        self.assertEqual(SimpleCalculate.subtract(5, 4), 1) 

    def test_multiply(self):
        self.assertEqual(SimpleCalculate.multiply(0, 4), 4)
        self.assertEqual(SimpleCalculate.multiply(4, 4), 0) 
        self.assertEqual(SimpleCalculate.multiply(5, 4), 1) 

    def test_divide(self):
        self.assertEqual(SimpleCalculate.divide(4, 4), 1)
        self.assertEqual(SimpleCalculate.divide(16, 4), 4)  
        self.assertEqual(SimpleCalculate.divide(4, 0), "Error: Cannot divide by zero.")                