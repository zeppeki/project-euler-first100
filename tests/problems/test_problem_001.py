"""Tests for Problem 001: Multiples of 3 and 5."""

import pytest
import sys
import os

# Add the problems directory to the path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..', 'problems'))

from problem_001 import solve_naive, solve_optimized, solve_mathematical


class TestProblem001:
    """Test cases for Problem 001."""

    def test_solve_naive(self):
        """Test the naive solution."""
        # Test cases: (limit, expected_result)
        test_cases = [
            (10, 23),      # 3 + 5 + 6 + 9 = 23
            (20, 78),      # 3 + 5 + 6 + 9 + 10 + 12 + 15 + 18 = 78
            (100, 2318),   # Known result for limit 100
        ]
        
        for limit, expected in test_cases:
            with self.subTest(limit=limit):
                result = solve_naive(limit)
                assert result == expected, f"Expected {expected}, got {result} for limit {limit}"

    def test_solve_optimized(self):
        """Test the optimized solution."""
        # Test cases: (limit, expected_result)
        test_cases = [
            (10, 23),      # 3 + 5 + 6 + 9 = 23
            (20, 78),      # 3 + 5 + 6 + 9 + 10 + 12 + 15 + 18 = 78
            (100, 2318),   # Known result for limit 100
        ]
        
        for limit, expected in test_cases:
            with self.subTest(limit=limit):
                result = solve_optimized(limit)
                assert result == expected, f"Expected {expected}, got {result} for limit {limit}"

    def test_solve_mathematical(self):
        """Test the mathematical solution."""
        # Test cases: (limit, expected_result)
        test_cases = [
            (10, 23),      # 3 + 5 + 6 + 9 = 23
            (20, 78),      # 3 + 5 + 6 + 9 + 10 + 12 + 15 + 18 = 78
            (100, 2318),   # Known result for limit 100
        ]
        
        for limit, expected in test_cases:
            with self.subTest(limit=limit):
                result = solve_mathematical(limit)
                assert result == expected, f"Expected {expected}, got {result} for limit {limit}"

    def test_all_solutions_agree(self):
        """Test that all solutions give the same result."""
        test_limits = [10, 20, 50, 100]
        
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
        assert solve_naive(2) == 0
        assert solve_optimized(2) == 0
        assert solve_mathematical(2) == 0

    @pytest.mark.slow
    def test_large_number(self):
        """Test with a large number (marked as slow)."""
        # Test with the actual problem limit
        limit = 1000
        expected = 233168
        
        result_naive = solve_naive(limit)
        result_optimized = solve_optimized(limit)
        result_math = solve_mathematical(limit)
        
        assert result_naive == expected
        assert result_optimized == expected
        assert result_math == expected

    def test_negative_input(self):
        """Test with negative input (should handle gracefully)."""
        # All solutions should handle negative input gracefully
        assert solve_naive(-10) == 0
        assert solve_optimized(-10) == 0
        assert solve_mathematical(-10) == 0