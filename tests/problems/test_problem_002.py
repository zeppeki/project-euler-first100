"""Tests for Problem 002: Even Fibonacci numbers."""

import os
import sys

import pytest

# Add the problems directory to the path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "..", "problems"))

# Import after path modification
from problems.problem_002 import solve_mathematical, solve_naive, solve_optimized


class TestProblem002:
    """Test cases for Problem 002."""

    @pytest.mark.parametrize(
        "limit,expected",
        [
            (10, 10),  # 2 + 8 = 10
            (50, 44),  # 2 + 8 + 34 = 44
            (100, 44),  # 2 + 8 + 34 = 44
        ],
    )
    def test_solve_naive(self, limit: int, expected: int) -> None:
        """Test the naive solution."""
        result = solve_naive(limit)
        assert result == expected, (
            f"Expected {expected}, got {result} for limit {limit}"
        )

    @pytest.mark.parametrize(
        "limit,expected",
        [
            (10, 10),  # 2 + 8 = 10
            (50, 44),  # 2 + 8 + 34 = 44
            (100, 44),  # 2 + 8 + 34 = 44
        ],
    )
    def test_solve_optimized(self, limit: int, expected: int) -> None:
        """Test the optimized solution."""
        result = solve_optimized(limit)
        assert result == expected, (
            f"Expected {expected}, got {result} for limit {limit}"
        )

    @pytest.mark.parametrize(
        "limit,expected",
        [
            (10, 10),  # 2 + 8 = 10
            (50, 44),  # 2 + 8 + 34 = 44
            (100, 44),  # 2 + 8 + 34 = 44
        ],
    )
    def test_solve_mathematical(self, limit: int, expected: int) -> None:
        """Test the mathematical solution."""
        result = solve_mathematical(limit)
        assert result == expected, (
            f"Expected {expected}, got {result} for limit {limit}"
        )

    @pytest.mark.parametrize("limit", [10, 50, 100, 400])
    def test_all_solutions_agree(self, limit: int) -> None:
        """Test that all solutions give the same result."""
        naive_result = solve_naive(limit)
        optimized_result = solve_optimized(limit)
        math_result = solve_mathematical(limit)

        assert naive_result == optimized_result == math_result, (
            f"Solutions disagree for limit {limit}: "
            f"naive={naive_result}, optimized={optimized_result}, math={math_result}"
        )

    def test_edge_cases(self) -> None:
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

    def test_negative_input(self) -> None:
        """Test with negative input (should handle gracefully)."""
        # All solutions should handle negative input gracefully
        assert solve_naive(-10) == 0
        assert solve_optimized(-10) == 0
        assert solve_mathematical(-10) == 0

    def test_problem_answer(self) -> None:
        """Test with the actual problem limit (optimized for speed)."""
        # Test with the actual problem limit
        limit = 4000000
        expected = 4613732

        # Only test mathematical solution for speed (fastest method)
        result_math = solve_mathematical(limit)
        assert result_math == expected

        # Quick verification with smaller test case that others agree
        small_limit = 100
        small_naive = solve_naive(small_limit)
        small_optimized = solve_optimized(small_limit)
        small_math = solve_mathematical(small_limit)
        assert small_naive == small_optimized == small_math
