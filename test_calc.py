import calc
import unittest


class TestClac(unittest.TestCase): #inheriting from unittest.TestCase allows you to have access to assert methods
    def test_add(self): #it should always start with test_...
        result = calc.add(5, 10)
        self.assertEqual(result,15)


    def test_subtract(self):
        result = calc.subtract(10,5)
        self.assertEqual(result, 5)

    def test_mult(self):
        result = calc.mult(10,5)
        self.assertEqual(result, 50)
        self.assertEqual(calc.mult(7,8), 56)

    def test_div(self):
        result = calc.div(10,5)
        self.assertEqual(result, 2)
        self.assertRaises(ValueError, calc.div, 10, 2) #this means that if by passing these two args to the function calc.div the exception will be raised or not!
        #if no exception is raised, then the test will be failed.
        self.assertRaises(ValueError, calc.div, 10 , 0)

