import unittest
from tdd_calculator import Calculator


class TestCalculator(unittest.TestCase):
    def setUp(self):
        self.calculator = Calculator()

    def test_addition(self):
        self.assertEquals(15, self.calculator.add(7, 8))
