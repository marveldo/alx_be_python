import unittest
from simple_calculator import SimpleCalculator

class TestSimpleCalculator(unittest.TestCase):

    def setUp(self):
        """Set up the SimpleCalculator instance before each test."""
        self.calc = SimpleCalculator()

    def test_addition(self):
        """Test the addition method."""
        self.assertEqual(self.calc.add(2, 3), 5)
        self.assertEqual(self.calc.add(-1, 1), 0)
        # Add more assertions to thoroughly test the add 
        self.assertEqual(self.calc.add(2,0), 2)

        self.assertEqual(self.calc.add(3,1),4)

    def test_subtraction(self):
        """Test Subtraction
        """
        self.assertEqual(self.calc.subtract(1,1), 0)
        self.assertEqual(self.calc.subtract(2,1), 1)
        self.assertEqual(self.calc.subtract(3,1) ,2)
    
    def test_multiplication(self):
        """Test Multiplication
        """

        self.assertEqual(self.calc.multiply(2,0), 0)
        self.assertEqual(self.calc.multiply(1,100), 100)
       
    
    def test_divide(self):
        """ Test Division"""
        self.assertEqual(self.calc.divide(100,20), 5)
        