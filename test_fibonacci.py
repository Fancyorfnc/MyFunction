"""
Unit tests for fibonacci module.
"""

import unittest
from fibonacci import (
    fibonacci_recursive,
    fibonacci_iterative,
    fibonacci_sequence,
    fibonacci_generator
)


class TestFibonacci(unittest.TestCase):
    """Test cases for Fibonacci implementations."""
    
    def test_fibonacci_iterative_base_cases(self):
        """Test base cases for iterative implementation."""
        self.assertEqual(fibonacci_iterative(0), 0)
        self.assertEqual(fibonacci_iterative(1), 1)
    
    def test_fibonacci_iterative_normal_cases(self):
        """Test normal cases for iterative implementation."""
        self.assertEqual(fibonacci_iterative(5), 5)
        self.assertEqual(fibonacci_iterative(10), 55)
        self.assertEqual(fibonacci_iterative(15), 610)
    
    def test_fibonacci_recursive_matches_iterative(self):
        """Test that recursive and iterative give same results."""
        for n in range(15):
            self.assertEqual(
                fibonacci_recursive(n),
                fibonacci_iterative(n),
                f"Mismatch at n={n}"
            )
    
    def test_fibonacci_sequence(self):
        """Test sequence generation."""
        self.assertEqual(fibonacci_sequence(0), [])
        self.assertEqual(fibonacci_sequence(1), [0])
        self.assertEqual(fibonacci_sequence(5), [0, 1, 1, 2, 3])
        self.assertEqual(fibonacci_sequence(10), [0, 1, 1, 2, 3, 5, 8, 13, 21, 34])
    
    def test_fibonacci_generator(self):
        """Test generator implementation."""
        result = list(fibonacci_generator(10))
        expected = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]
        self.assertEqual(result, expected)
    
    def test_negative_input_raises_error(self):
        """Test that negative inputs raise ValueError."""
        with self.assertRaises(ValueError):
            fibonacci_iterative(-1)
        with self.assertRaises(ValueError):
            fibonacci_recursive(-1)
        with self.assertRaises(ValueError):
            fibonacci_sequence(-1)
        with self.assertRaises(ValueError):
            list(fibonacci_generator(-1))


if __name__ == '__main__':
    unittest.main()
