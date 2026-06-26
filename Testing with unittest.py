import unittest

# Function to test
def add(a, b):
    return a + b

def divide(a, b):
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b

# Test class
class TestMathOperations(unittest.TestCase):
    def test_add(self):
        self.assertEqual(add(2, 3), 5)
        self.assertEqual(add(-1, 1), 0)
    
    def test_add_floats(self):
        self.assertAlmostEqual(add(0.1, 0.2), 0.3, places=7)
    
    def test_divide(self):
        self.assertEqual(divide(10, 2), 5)
    
    def test_divide_by_zero(self):
        with self.assertRaises(ValueError):
            divide(10, 0)

# Run tests
if __name__ == "__main__":
    unittest.main()

# Other useful assertions:
# self.assertTrue(x)
# self.assertFalse(x)
# self.assertIsNone(x)
# self.assertIn(a, b)
# self.assertIsInstance(a, b)
