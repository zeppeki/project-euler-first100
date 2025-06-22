"""Tests for Problem 002: Even Fibonacci numbers."""

import pytest
import sys
import os

# Add the problems directory to the path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..', 'problems'))

from problem_002 import solve_naive, solve_optimized, solve_mathematical


class TestProblem002:
    """Test cases for Problem 002."""

    def test_solve_naive(self):
        """Test the naive solution."""
        # Test cases: (limit, expected_result)
        test_cases = [
            (10, 10),      # 2 + 8 = 10
            (50, 44),      # 2 + 8 + 34 = 44
            (100, 44),     # 2 + 8 + 34 = 44
        ]
        
        for limit, expected in test_cases:
            with self.subTest(limit=limit):
                result = solve_naive(limit)
                assert result == expected, f"Expected {expected}, got {result} for limit {limit}"

    def test_solve_optimized(self):
        """Test the optimized solution."""
        # Test cases: (limit, expected_result)
        test_cases = [
            (10, 10),      # 2 + 8 = 10
            (50, 44),      # 2 + 8 + 34 = 44
            (100, 44),     # 2 + 8 + 34 = 44
        ]
        
        for limit, expected in test_cases:
            with self.subTest(limit=limit):
                result = solve_optimized(limit)
                assert result == expected, f"Expected {expected}, got {result} for limit {limit}"

    def test_solve_mathematical(self):
        """Test the mathematical solution."""
        # Test cases: (limit, expected_result)
        test_cases = [
            (10, 10),      # 2 + 8 = 10
            (50, 44),      # 2 + 8 + 34 = 44
            (100, 44),     # 2 + 8 + 34 = 44
        ]
        
        for limit, expected in test_cases:
            with self.subTest(limit=limit):
                result = solve_mathematical(limit)
                assert result == expected, f"Expected {expected}, got {result} for limit {limit}"

    def test_all_solutions_agree(self):
        """Test that all solutions give the same result."""
        test_limits = [10, 50, 100, 400]
        
        for limit in test_limits:
            with self.subTest(limit=limit):
                naive_result = solve_naive(limit)
                optimized_result = solve_optimized(limit)
                math_result = solve_mathematical(limit)
                
                assert naive_result == optimized_result == math_result, (
                    f"Solutions disagree for limit {limit}: "
                    f"naive={naive_result}, optimized={optimized_result}, math={math_result}"
                )

    def test_edge_cases(self):
        """Test edge cases."""
        # Test with limit 0
        assert solve_naive(0) == 0
        assert solve_optimized(0) == 0
        assert solve_mathematical(0) == 0
        
        # Test with limit 1
        assert solve_naive(1) == 0
        assert solve_optimized(1) == 0
        assert solve_mathematical(1) == 0
        
        # Test with limit 2
        assert solve_naive(2) == 2
        assert solve_optimized(2) == 2
        assert solve_mathematical(2) == 2

    @pytest.mark.slow
    def test_large_number(self):
        """Test with a large number (marked as slow)."""
        # Test with the actual problem limit
        limit = 4000000
        expected = 4613732
        
        result_naive = solve_naive(limit)
        result_optimized = solve_optimized(limit)
        result_math = solve_mathematical(limit)
        
        assert result_naive == expected
        assert result_optimized == expected
        assert result_math == expected 