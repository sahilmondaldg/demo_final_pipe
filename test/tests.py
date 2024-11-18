import unittest
from calculator.operations import add, subtract, multiply, divide

class TestOperations(unittest.TestCase):
    
    def testAdd(self):
        self.assertEqual(add(3,4), 7)
        self.assertEqual(add(-1,-1), -2)
        self.assertEqual(add(3,-2), 1)

    def testSubtract(self):
        self.assertEqual(subtract(5,1), 4)
        self.assertEqual(subtract(3,-2), 5)
        self.assertEqual(subtract(-3,-4), 1)

    def testMultiply(self):
        self.assertEqual(multiply(2,3), 6)
        self.assertEqual(multiply(-7,-2), 14)
        self.assertEqual(multiply(3,-9), -27)

    def testDivide(self):
        self.assertEqual(divide(6,2), 3)
        self.assertEqual(divide(-27,-3), 9)
        self.assertEqual(divide(-18,3), -6)

if __name__=="__main__":
    unittest.main()