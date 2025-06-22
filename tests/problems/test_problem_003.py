"""Tests for Problem 003: Largest prime factor."""

import pytest
import sys
import os

# Add the problems directory to the path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..', 'problems'))

from problem_003 import solve_naive, solve_optimized, solve_mathematical


class TestProblem003:
    """Test cases for Problem 003."""

    def test_solve_naive(self):
        """Test the naive solution."""
        # Test cases: (n, expected_result)
        test_cases = [
            (13195, 29),      # Example: 5, 7, 13, 29 → max is 29
            (100, 5),         # 100 = 2^2 × 5^2 → max is 5
            (84, 7),          # 84 = 2^2 × 3 × 7 → max is 7
        ]
        
        for n, expected in test_cases:
            with self.subTest(n=n):
                result = solve_naive(n)
                assert result == expected, f"Expected {expected}, got {result} for n={n}"

    def test_solve_optimized(self):
        """Test the optimized solution."""
        # Test cases: (n, expected_result)
        test_cases = [
            (13195, 29),      # Example: 5, 7, 13, 29 → max is 29
            (100, 5),         # 100 = 2^2 × 5^2 → max is 5
            (84, 7),          # 84 = 2^2 × 3 × 7 → max is 7
        ]
        
        for n, expected in test_cases:
            with self.subTest(n=n):
                result = solve_optimized(n)
                assert result == expected, f"Expected {expected}, got {result} for n={n}"

    def test_solve_mathematical(self):
        """Test the mathematical solution."""
        # Test cases: (n, expected_result)
        test_cases = [
            (13195, 29),      # Example: 5, 7, 13, 29 → max is 29
            (100, 5),         # 100 = 2^2 × 5^2 → max is 5
            (84, 7),          # 84 = 2^2 × 3 × 7 → max is 7
        ]
        
        for n, expected in test_cases:
            with self.subTest(n=n):
                result = solve_mathematical(n)
                assert result == expected, f"Expected {expected}, got {result} for n={n}"

    def test_all_solutions_agree(self):
        """Test that all solutions give the same result."""
        test_cases = [13195, 100, 84, 17, 25]
        
        for n in test_cases:
            with self.subTest(n=n):
                naive_result = solve_naive(n)
                optimized_result = solve_optimized(n)
                math_result = solve_mathematical(n)
                
                assert naive_result == optimized_result == math_result, (
                    f"Solutions disagree for n={n}: "
                    f"naive={naive_result}, optimized={optimized_result}, math={math_result}"
                )

    def test_edge_cases(self):
        """Test edge cases."""
        # Test with n = 0
        assert solve_naive(0) == 0
        assert solve_optimized(0) == 0
        assert solve_mathematical(0) == 0
        
        # Test with n = 1
        assert solve_naive(1) == 1
        assert solve_optimized(1) == 1
        assert solve_mathematical(1) == 1
        
        # Test with n = 2 (prime)
        assert solve_naive(2) == 2
        assert solve_optimized(2) == 2
        assert solve_mathematical(2) == 2

    def test_prime_numbers(self):
        """Test with prime numbers."""
        prime_numbers = [17, 19, 23, 29, 31]
        
        for prime in prime_numbers:
            with self.subTest(prime=prime):
                assert solve_naive(prime) == prime
                assert solve_optimized(prime) == prime
                assert solve_mathematical(prime) == prime

    @pytest.mark.slow
    def test_large_number(self):
        """Test with a large number (marked as slow)."""
        # Test with the actual problem number
        n = 600851475143
        expected = 6857
        
        # Only test optimized and mathematical solutions as naive is too slow
        result_optimized = solve_optimized(n)
        result_math = solve_mathematical(n)
        
        assert result_optimized == expected
        assert result_math == expected 